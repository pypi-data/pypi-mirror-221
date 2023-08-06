from alive_progress import alive_bar
from alive_progress import alive_it
from collections import defaultdict
from collections import OrderedDict
from itertools import combinations
import click
import filecmp
import hashlib
import os

def chunk_reader(fobj, chunk_size):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def get_hash(filename, first_chunk_only=False, hash=hashlib.sha1, chunk_size=1024):
    """Get hash of file or hash of first chunk of file"""
    hashobj = hash()
    try:
        with open(filename, "rb") as f:
            if first_chunk_only:
                hashobj.update(f.read(chunk_size))
            else:
                for chunk in chunk_reader(f, chunk_size):
                    hashobj.update(chunk)
    except OSError:
        # not accessible (permissions, etc) - pass on
        return None
    return hashobj.digest()

def path_to_real_and_relative(path, dir=os.curdir):
    """Get realpath and path relative to dir"""
    try:
        # if the target is a symlink (soft one), this will
        # dereference it - change the value to the actual target file
        realpath = os.path.realpath(path, strict=True)
        relpath = os.path.relpath(realpath, dir)
    except OSError:
        # not accessible (permissions, etc) - pass on
        return None
    return realpath, relpath

def translate_to_paths(subdirpath, filenames, dir=os.curdir):
    for name in filenames:
        fullpath = os.path.join(subdirpath, name)
        path_tuple = path_to_real_and_relative(fullpath, dir)
        yield path_tuple

def paths_to_realpaths(paths):
    """Map realpaths of all paths passed in"""
    realpaths = OrderedDict()
    for path in paths:
        realpath, relpath = path_to_real_and_relative(path)
        assert(relpath == path)
        realpaths[realpath] = relpath
    return realpaths

def get_files_from_dir(dir):
    """Get real paths of all files in a directory"""
    paths = OrderedDict()
    with alive_bar(spinner=None) as bar:
        for subdirpath, _, files in os.walk(dir):
            for realpath, relpath in translate_to_paths(subdirpath, files, dir):
                paths[(dir, relpath)] = realpath
                bar()
    return paths

def compare_dir_structures(dir1, dir2):
    """Classify paths according to whether they are in dir1 only, dir2 only, or both"""
    paths = OrderedDict()
    paths_only_in_dir1 = []
    paths_only_in_dir2 = []
    files_in_both = []

    with alive_bar(spinner=None) as bar:
        for (subdirpath1, subdirs1, files1), (subdirpath2, subdirs2, files2) in zip(os.walk(dir1), os.walk(dir2)):
            def path_helper(subdirpath, pathset, dir, category):
                for realpath, relpath in translate_to_paths(subdirpath, pathset, dir):
                    category.append(relpath)
                    paths[(dir, relpath)] = realpath
                    bar()

            f1, f2 = set(files1), set(files2)
            s1, s2 = set(subdirs1), set(subdirs2)

            # Use set difference to find paths that are only in one directory
            path_helper(subdirpath1, f1 - f2, dir1, paths_only_in_dir1)
            path_helper(subdirpath1, s1 - s2, dir1, paths_only_in_dir1)
            path_helper(subdirpath2, f2 - f1, dir2, paths_only_in_dir2)
            path_helper(subdirpath2, s2 - s1, dir2, paths_only_in_dir2)

            # Use set intersection to find paths that are in both directories
            t1 = translate_to_paths(subdirpath1, f1 & f2, dir1)
            t2 = translate_to_paths(subdirpath2, f1 & f2, dir2)
            for (realpath1, relpath1), (realpath2, relpath2) in zip(t1, t2):
                assert(relpath1 == relpath2)
                files_in_both.append(relpath1)
                paths[(dir1, relpath1)] = realpath1
                bar()
                paths[(dir2, relpath2)] = realpath2
                bar()

            # Only continue to traverse the common sub directories
            subdirs_in_both = s1 & s2
            subdirs1[:] = subdirs2[:] = subdirs_in_both

    return paths, paths_only_in_dir1, paths_only_in_dir2, files_in_both

def find_duplicates_impl(dirs, hash=hashlib.sha1):
    files = []                              # [ realpath1, realpath2, ]
    for dir, reldir in paths_to_realpaths(dirs).items():
        click.echo(f"Fetching files from {reldir}")
        paths = get_files_from_dir(dir)
        files.extend(paths.values())

    size_to_file = defaultdict(list)        # { file_size: [ realpath_to_file1, realpath_to_file2, ] }
    small_hash_to_file = defaultdict(list)  # { (small_hash, file_size): [ realpath_to_file1, realpath_to_file2, ] }
    full_hash_to_file = defaultdict(list)   # { full_hash: [ realpath_to_file1, realpath_to_file2, ] }

    click.echo("Fetching file sizes")
    for filepath in alive_it(files, spinner=None):
        # Group files that have the same size - they are the collision candidates
        try:
            file_size = os.path.getsize(filepath)
        except OSError:
            # not accessible (permissions, etc) - pass on
            continue
        size_to_file[file_size].append(filepath)

    click.echo("Computing small hashes")
    total_files = sum(len(files) for files in size_to_file.values() if len(files) > 1)
    with alive_bar(total_files, spinner=None) as bar:
        # For all files with the same file size, get their hash on the 1st 1024 bytes only
        for file_size, files in size_to_file.items():
            assert(len(files) > 0)
            if len(files) == 1:
                # This file size is unique, no need to spend cpu cycles on it
                continue

            for filepath in files:
                small_hash = get_hash(filepath, first_chunk_only=True)
                # Map from hash of 1024 bytes and the file size - to avoid collisions on equal hashes in the first part
                # of the file
                # credits to @Futal for the optimization
                small_hash_to_file[(small_hash, file_size)].append(filepath)
                bar()

    click.echo("Computing full hashes")
    total_files = sum(len(files) for files in small_hash_to_file.values() if len(files) > 1)
    with alive_bar(total_files, spinner=None) as bar:
        # For all files with the hash on the 1st 1024 bytes, get their hash on the full file
        for files in small_hash_to_file.values():
            assert(len(files) > 0)
            if len(files) == 1:
                # This hash/file_size combination is unique, no need to spend cpu cycles on it
                continue

            for filepath in files:
                full_hash = get_hash(filepath)
                full_hash_to_file[full_hash].append(filepath)
                bar()

    dup_stats = []
    for files in full_hash_to_file.values():
        if len(files) > 1:
            dup_stats.append([path_to_real_and_relative(file)[1] for file in files])
    return dup_stats

def compare_directories_impl(dirs):
    diff_stats = OrderedDict()  # { (dir1, dir2): (files_only_in_dir1, files_only_in_dir2, files_do_not_match) }

    for (dir1, reldir1), (dir2, reldir2) in combinations(paths_to_realpaths(dirs).items(), 2):
        click.echo(f"Comparing directories {reldir1} and {reldir2}")
        click.echo("Comparing directory structures")
        paths, paths_only_in_dir1, paths_only_in_dir2, files_in_both = compare_dir_structures(dir1, dir2)

        files_do_not_match = []
        click.echo("Comparing common files")
        for f in alive_it(files_in_both, spinner=None):
            assert((dir1, f) in paths)
            assert((dir2, f) in paths)
            realpath1 = paths[(dir1, f)]
            realpath2 = paths[(dir2, f)]
            # Compare the files byte-by-byte
            # Note: filecmp.cmpfiles would be better but we can't track progress with a progress bar
            if not filecmp.cmp(realpath1, realpath2, shallow=False):
                files_do_not_match.append(f)
        diff_stats[(reldir1, reldir2)] = (paths_only_in_dir1, paths_only_in_dir2, files_do_not_match)

    return diff_stats

@click.group
def cli():
    pass

@cli.command()
@click.argument("dirs", type=click.Path(exists=True, file_okay=False), nargs=-1)
def find_duplicates(dirs):
    for files in find_duplicates_impl(dirs):
        click.echo("")
        click.echo("Duplicates found:")
        filestr = '\n'.join(files)
        click.echo(f"{filestr}")
        click.echo("")

@cli.command()
@click.argument("dirs", type=click.Path(exists=True, file_okay=False), nargs=-1)
def compare_directories(dirs):
    for (dir1, dir2), (files_dir1, files_dir2, files_not_matching) in compare_directories_impl(dirs).items():
        click.echo("")
        click.echo(f"Files found in {dir1} but not found in {dir2}:")
        filenamestr = '\n'.join(files_dir1)
        click.echo(f"{filenamestr}")
        click.echo("")

        click.echo(f"Files found in {dir2} but not found in {dir1}:")
        filenamestr = '\n'.join(files_dir2)
        click.echo(f"{filenamestr}")
        click.echo("")

        click.echo(f"Files found in {dir1} and {dir2} but contents do not match:")
        filestr = '\n'.join(files_not_matching)
        click.echo(f"{filestr}")
        click.echo("")

if __name__ == "__main__":
    cli()

# pathdiff

[![PyPI - Version](https://img.shields.io/pypi/v/pathdiff.svg)](https://pypi.org/project/pathdiff)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pathdiff.svg)](https://pypi.org/project/pathdiff)

Pathdiff is a tool for:

1. Detecting duplicate files in directories (Based on https://stackoverflow.com/a/36113168/300783)
2. Comparing directories for differences in structure and content

There are a number of alternative tools for both usecases, but this is a simple
implementation that can be easily modified (unlike complex gui tools) and
provides small conveniences like progress bars (unlike more basic command line
tools like diff).

---

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install pathdiff
```

## Usage

```console
❯ pathdiff find-duplicates tests/test1
Fetching files from tests/test1
|████████████████████████████████████████| 9 in 0.1s (88.59/s)
Fetching file sizes
|████████████████████████████████████████| 9/9 [100%] in 0.1s (88.10/s)
Computing small hashes
|████████████████████████████████████████| 9/9 [100%] in 0.1s (88.25/s)
Computing full hashes
|████████████████████████████████████████| 9/9 [100%] in 0.1s (88.01/s)

Duplicates found:
tests/test1/f2/file7.txt
tests/test1/f1/file4.txt


Duplicates found:
tests/test1/f1/file2.txt
tests/test1/f1/file3.txt
tests/test1/f1/file1.txt


Duplicates found:
tests/test1/f2/file8.txt
tests/test1/f2/file9.txt


Duplicates found:
tests/test1/f1/file5.txt
tests/test1/f1/file6.txt
```

```console
❯ pathdiff compare-directories tests/test2/path1 tests/test2/path2
Comparing directories tests/test2/path1 and tests/test2/path2
Comparing directory structures
|████████████████████████████████████████| 28 in 0.1s (265.55/s)
Comparing common files
|████████████████████████████████████████| 9/9 [100%] in 0.1s (85.30/s)

Paths found in tests/test2/path1 but not found in tests/test2/path2:
file3-1.txt
f6/f1-1
f5/f1/file7-1.txt
f1/file3-1.txt
f1/f1/file3-1.txt

Paths found in tests/test2/path2 but not found in tests/test2/path1:
file3-2.txt
f6/f1-2
f5/f1/file7-2.txt
f1/file3-2.txt
f1/f1/file3-2.txt

Files found in tests/test2/path1 and tests/test2/path2 but contents do not match:
file2.txt
f4/f1/file6.txt
f1/file2.txt
f1/f1/file2.txt
```

```console
❯ pathdiff compare-contents tests/test3/path1 tests/test3/path2
Comparing contents in directories tests/test3/path1 and tests/test3/path2
Fetching files from tests/test3/path1
|████████████████████████████████████████| 12 in 0.1s (118.00/s)
Fetching files from tests/test3/path2
|████████████████████████████████████████| 8 in 0.1s (77.02/s)
Fetching file sizes
|████████████████████████████████████████| 20/20 [100%] in 0.1s (196.16/s)
Computing small hashes
|████████████████████████████████████████| 20/20 [100%] in 0.1s (196.73/s)
Computing full hashes
|████████████████████████████████████████| 16/16 [100%] in 0.1s (155.59/s)

Files found in tests/test3/path1 but not found in tests/test3/path2 (by content, names may match):
f1/f1/file5.txt
f1/f1/file4-1.txt

Files found in tests/test3/path2 but not found in tests/test3/path1 (by content, names may match):
file5.txt
file4-2.txt

Files which do not match one-to-one or have different names:
Group of duplicate files:
Duplicates from tests/test3/path1:
file7.txt
f1/f1/file7.txt
Duplicates from tests/test3/path2:

Group of duplicate files:
Duplicates from tests/test3/path1:
file9-1.txt
f1/f1/file9.txt
Duplicates from tests/test3/path2:
file9.txt
Group of duplicate files:
Duplicates from tests/test3/path1:
file8.txt
f1/f1/file8.txt
Duplicates from tests/test3/path2:
file8.txt
Group of duplicate files:
Duplicates from tests/test3/path1:
f1/f1/file6-1.txt
Duplicates from tests/test3/path2:
file6-2.txt
```

## License

`pathdiff` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

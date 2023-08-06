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

-----

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
|████████████████████████████████████████| 9 in 0.1s (85.56/s)
Fetching file sizes
|████████████████████████████████████████| 9/9 [100%] in 0.1s (87.68/s)
Computing small hashes
|████████████████████████████████████████| 9/9 [100%] in 0.1s (85.21/s)
Computing full hashes
|████████████████████████████████████████| 9/9 [100%] in 0.1s (83.98/s)

Duplicates found:
tests/test1/path1/file2.txt
tests/test1/path1/file3.txt
tests/test1/path1/file1.txt


Duplicates found:
tests/test1/path1/file4.txt
tests/test1/path2/file7.txt


Duplicates found:
tests/test1/path1/file5.txt
tests/test1/path1/file6.txt


Duplicates found:
tests/test1/path2/file8.txt
tests/test1/path2/file9.txt
```

```console
❯ pathdiff compare-directories tests/test2/path1 tests/test2/path2
Comparing directories tests/test2/path1 and tests/test2/path2
Comparing directory structures
|████████████████████████████████████████| 12 in 0.1s (114.04/s)
Comparing common files
|████████████████████████████████████████| 4/4 [100%] in 0.1s (37.66/s)

Files found in tests/test2/path1 but not found in tests/test2/path2:
file2.txt
file1.txt

Files found in tests/test2/path2 but not found in tests/test2/path1:
file8.txt
file7.txt

Files found in tests/test2/path1 and tests/test2/path2 but contents do not match:
file5.txt
file6.txt
```

## License

`pathdiff` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

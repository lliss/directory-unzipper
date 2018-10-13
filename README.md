# Directory Unzipper

A simple python script to unzip an entire directory of zip files.

This can be called from within a directory and it will run on the files in that directory...

```
$ cd /path/to/zip-dir
$ ls
file1.zip file2.zip

$ py /path/to/dirunzip.py
$ ls
file1zip file2zip file1.zip file2.zip
```

It can also be called with command line arguments...

```
$ ls /path/to/zip-dir
file1.zip file2.zip

$ py dirunzip.py /path/to/zip-dir
$ ls /path/to/zip-dir
file1zip file2zip file1.zip file2.zip
```

An additional `-r` or `--remove` flag can be set to remove the original zip files after extraction.

```
$ ls /path/to/zip-dir
file1.zip file2.zip

$ py dirunzip.py /path/to/zip-dir -r
$ ls /path/to/zip-dir
file1zip file2zip
```

For those on POSIX based systems, the `dirunzip` script can be made executable and added to your path to allow simply running

`dirunzip`

from anywhere on the system. This greatly simplifies the use.

## Versions and support

This has been test on Windows, MacOS, and Linux in Python versions 2 and 3. Python 3 produces better output messages but the functionality is otherwise identical.

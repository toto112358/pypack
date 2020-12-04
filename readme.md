# PYPACK !!!
Just a simple python3 package manager & compiler

Compiling python3 programs to ELF makes them considerably faster.

Install:
--------
Run `sudo make dependencies` to install all required packages, then `sudo make install` to install pypack.

Uninstall:
---------
Run `sudo make uninstall`

Usage:
------
Run `sudo pypack -h` to get all commands. Here are a few basic examples:

Run `sudo pypack -i foo -f foo.py` to **install** `foo.py` as the command `foo`

Run `sudo pypack -p foo` to **uninstall** the `foo` package you just installed

Run `sudo pypack -p '*'` *(or `sudo pypack -p \*`)* in order to uninstall **ALL** pypack packages (except pypack, py2elf)

Known issues:
------------
- Update package not coded yet
- `pypack -p *` won't work since bash interprets `*` as everything. So you have to escape the `*` character

To do:
------
1. Add option to detect python3 version installed
2. Add dependencies support (e.g. a python package can be dependant on another one)
3. Create a .PYPACK package extention
    - Dependencies support
    - Instructions to install and/or uninstall properly
5. Add package versionning to downgrade packages to backed-up versions
6. Add seamless package install by installing all packages in a pypack directory but creating symbolic links
7. Add a --update option to update python3 program
8. Add a [cheat sheet](cheat_sheet.md)
9. Add an option to show all installed packages
10. Add a package repository
11. Ask community to make commits on my script
12. Add support for python3 project that need MULTIPLE files
13. Add some VIM propaganda in easter eggs





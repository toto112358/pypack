# PYPACK !!!
Just a simple python3 package manager & compiler. It doesn't even require root access!!!

Compiling python3 programs to ELF makes them considerably faster.

Compiling
---------
Run `make` to compile it to a 64-bit .deb package you can later install

Run `make clean` to remove all compiled binaries

Install:
--------
Two ways:
- Run `sudo make dependencies` to install all required packages, then `sudo make install` to install pypack.
- Or run `sudo make dependencies && make && dpkg -i pypack.deb && make clean` on debian-based distributions.

Uninstall:
---------
Run `sudo make uninstall` or if you installed it via dpkg run `sudo dpkg --purge pypack && sudo rm -r /opt/pypack`

Usage:
------
Run `pypack -h` to get all commands. Here are a few basic examples:

Run `pypack -i foo -f foo.py` to **install** `foo.py` as the command `foo`

Run `pypack -p foo` to **uninstall** the `foo` package you just installed

Run `pypack -p '*'` *(or `pypack -p \*`)* in order to uninstall **ALL** pypack packages (except pypack, py2elf)

Known issues:
------------
- Update package not coded yet
- `pypack -p *` won't work since bash interprets `*` as everything. So you have to escape the `*` character

To do:
------
1. Add dependencies support (e.g. a python package can be dependant on another one)
3. Add configuration file to customize install (i.e. install root version or non-root)
4. Create a .PYPACK package extention
    - Dependencies support
    - Instructions to install and/or uninstall properly
5. ~Add package versionning to downgrade packages to backed-up versions~ (maybe not a good indea)
7. **Add a --update option to update python3 program** (URGENT)
8. Add a [cheat sheet](cheat_sheet.md)
9. Add an option to show all installed packages (PRIORITY)
10. Add a package repository
11. Ask community to make commits on my script
12. Add support for python3 project that need MULTIPLE files
13. Add some VIM propaganda in easter eggs





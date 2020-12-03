# PYPACK !!!
Just a simple python3 package manager & compiler

Install:
--------
Run `sudo make dependencies` to install all required packages, then `sudo make install` to install pypack.

Uninstall:
---------
Run `sudo make uninstall`

Usage:
------
Run `sudo pypack -h` to get all commands. Here are a few basic examples:

Run `sudo pypack -i foo -f foo.py` to install `foo.py` as the command `foo`

Run `sudo pypack -p foo` to uninstall the `foo` package you just installed

Known issues:
------------
- ~Somehow, the pypack script will NEVER be able to compile a python file, even when I make it using the working py2elf script~
    - EDIT : it was just me who was using my own script the wrong way

To do:
------
1. Add option to detect python3 version installed
2. Add seamless package install by installing all packages in a pypack directory but creating symbolic links
3. Add a --update option to update python3 program
4. Add a [cheat sheet](cheat_sheet.md)
5. Add an option to show all installed packages
6. Make pypack **fool-proof**
7. Ask community to make commits on my script
8. Add support for python3 project that need MULTIPLE files
9. Add some VIM propaganda in easter eggs





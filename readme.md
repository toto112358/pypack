# PYPACK !!!
Just a simple python3 package manager & compiler. It doesn't even require root access!!!

Compiling python3 programs to ELF makes them considerably faster.

Check out our new [repository](https://github.com/toto112358/pypack-repo)


Compiling
---------
Run `make deb` to compile it to a 64-bit .deb package you can later install

Run `make clean` to remove all compiled binaries

Install:
--------
### Debian-based distros
- ~Run `make dependencies && make && dpkg -i pypack.deb && make clean` on debian-based distributions.~

-> Instead, run `make stupid_install`

### Any other distros
- Run `make -s print_dependencies` and pipe the output with `xargs` to the package manager of your choice or install them manually.
- Then run `make install`.

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
- `pypack -p *` won't work since `*` is a special character.

To do:
------
1. Add dependencies support (e.g. a python package can be dependant on another one)
3. Make pypack installation for ALL users instead of current user only
4. Add configuration file to customize install (i.e. install root version or non-root)
5. Create a .PYPACK package extention
    - Dependencies support
    - Instructions to install and/or uninstall properly
6. ~Add package versionning to downgrade packages to backed-up versions~ (maybe not a good indea)
8. Add a [cheat sheet](cheat_sheet.md)
	- edit: I want this software to be so stupid that a cheat cheat wont be necessary
10. Add an option to show all installed packages (PRIORITY)
11. Add a package repository
    - `pypack repo install [pkg name]` would download and install [pkg name]
    - Or a `pyget` command would do the job.
12. Ask community to make commits on my script
13. Add support for python3 project that need MULTIPLE files
14. Add some VIM propaganda in easter eggs

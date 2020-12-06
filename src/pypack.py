#!/usr/bin/python3
# Package manager for python3 binaries compiled to ELF
import argparse
import os
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str 

def pkg_add(pkg,packagelst):                                        # pkg_add pkg full location + full path to package.lst
    with open(packagelst, 'a') as f:
        f.write(pkg+'\n')

def pkg_purge(pkg,packagelst):
    package_installed=False                                         # FOOL PROOF: check if pkg already installed
    with open(packagelst, 'r') as f:
        lines=f.readlines()
    with open(packagelst, 'w') as f:
        for line in lines:
            if line.strip('\n')  != pkg:
                f.write(line)
            else:
                package_installed=True
    if package_installed:
        os.system(f'rm {pkg}')
        

def pkg_purge_all(packagelst):
    exceptions=[]                                                   # List of packages we skipped (pypack, py2elf by default)
    print('removing all pypack packages excluding pypack, py2elf')
    with open(packagelst, 'r') as f:
        for line in f.readline():
            if line[-6:] == 'pypack' or line[:-6] == 'py2elf':
                exceptions.append(line)
                os.system(f'rm {line}')
    os.system(f'rm {packagelst} && touch {packagelst}')
    with open(packagelst,'w') as f:
        for line in exceptions:
            f.write(line)
    
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
def py2elf(imput,output):
    if os.path.isfile('/opt/pypack/bin/py2elf'):                           # if py2elf installed
        os.system(f'py2elf -o {output} {imput}') 
    elif os.path.isfile('./py2elf.py'):                                # if py2elf installed
        os.system(f'./py2elf.py -o {output} {imput}')               # if py2elf in same directory
    else:
        exit('py2elf not found')


pypack_dir='/var/lib/pypack/'                                       # Directory where we will have necessary files for pypack to work properly
pypack_packagelst='packages.lst'                                    # File where all stored packages are listed
pypath=os.popen('which python3').read()[:-1]                         # Py3 directory
working_dir=os.popen('pwd').read()[:-1]
#if os.geteuid() == 0:
#    exit("You don't need to have root privileges to run this script.\nPlease try again this time without 'sudo'. Exiting")


parser=argparse.ArgumentParser()
parser.add_argument('-i', help='specify name of the package to install (e.g. pypack -i foo -f bar.py will install bar.py and it will be installed in /opt/pypack/bin/foo)')
parser.add_argument('-f', help='specify the python3 package to install or update')
parser.add_argument('-p', '--purge', help='uninstall specified package (uninstalling package \\* is equivalent to removing all packages but py2elf and pypack)')
parser.add_argument('-u', '--update', help='specify the name of the package to update')
parser.add_argument('-n', '--no-compile', help='if --no-compile is specified, the script will be installed without being compiled',action='count')
args=parser.parse_args()

# PART OF CODE TO INSTALL PACKAGE
# -------------------------------

if args.i and not bool(args.no_compile) and args.f:                            # Here we do compile the python file to an ELF
    out_file=args.i
    in_file=args.f
    temp_file='/tmp/out'+get_random_string(20)
    if os.path.isfile(f'/opt/pypack/bin/{out_file}'):                      # if file exists: exit with error
        exit(f'[error] /opt/pypack/bin/{out_file} exists!')
    py2elf(working_dir+'/'+in_file,temp_file)
    os.system(f'chmod +x {temp_file} && mv {temp_file} /opt/pypack/bin/{out_file}')
    pkg_add(f'/opt/pypack/bin/{out_file}',pypack_dir+pypack_packagelst)    # NEED TO ADD THE INSTALLED PACKAGE TO PACKAGE.LST FOR LATER UNINSTALL !!!

if args.i and bool(args.no_compile) and args.f:                                # Here we don't compile the python file to an ELF
    out_file=args.i
    in_file=args.f
    with open(in_file,'r') as f:
        line1=f.readline()
        if '#!/opt/pypack/bin/python' in line1:
            #thats cool
            print(f'{line1} in 1st line. that\'s cool!')
        else:
            #thats not cool
            #Let's suppose we use python3
            line_prepender(in_file,f'#!{pypath}')
    if os.path.isfile(f'/opt/pypack/bin/{out_file}'):                      # if file exists: exit with error
        exit(f'[error] /opt/pypack/bin/{out_file} exists!')
    os.system(f'chmod +x {in_file} && cp {in_file} /opt/pypack/bin/{out_file}')
    pkg_add(f'/opt/pypack/bin/{out_file}',pypack_dir+pypack_packagelst)    # NEED TO ADD THE INSTALLED PACKAGE TO PACKAGE.LST FOR LATER UNINSTALL !!!

# PART OF CODE TO REMOVE PACKAGE
# ------------------------------
if args.purge:
    pkg2purge=args.purge
    if pkg2purge == '*':                                            # We remove ALL installed pkg
        pkg_purge_all(pypack_dir+pypack_packagelst)
    else:                                                           # We only remove specified pkg
        pkg_purge(f'/opt/pypack/bin/{pkg2purge}',pypack_dir+pypack_packagelst) 

# PART OF CODE TO UPDATE EXISTING PACKAGE
# ---------------------------------------
if args.update and args.f and not bool(args.no_compile):                # Here we compile to ELF
    # need to check if package is installed
    # if not installed : error
    # Yes ? Ok. Then proceed to installation
    # if package is py2elf or pypack, display warning + confirmation
    out_file=args.update
    in_file=args.f
    temp_file='/tmp/out'+get_random_string(20)
    if not os.path.isfile(f'/opt/pypack/bin/{out_file}'):                      # if file exists: exit with error
        exit(f'[error] /opt/pypack/bin/{out_file} doesn\'t exist!')
    py2elf(working_dir+'/'+in_file,temp_file)
    os.system(f'chmod +x {temp_file} && mv {temp_file} /opt/pypack/bin/{out_file}')
    pkg_add(f'/opt/pypack/bin/{out_file}',pypack_dir+pypack_packagelst)    # NEED TO ADD THE INSTALLED PACKAGE TO PACKAGE.LST FOR LATER UNINSTALL !!!

if args.update and bool(args.no_compile) and args.f:                                # Here we don't compile the python file to an ELF
    out_file=args.update
    in_file=args.f
    with open(in_file,'r') as f:
        line1=f.readline()
        if '#!/opt/pypack/bin/python' in line1:
            #thats cool
            print(f'{line1} in 1st line. that\'s cool!')
        else:
            #thats not cool
            #Let's suppose we use python3
            line_prepender(in_file,f'#!{pypath}')
    if not os.path.isfile(f'/opt/pypack/bin/{out_file}'):                      # if file exists: exit with error
        exit(f'[error] /opt/pypack/bin/{out_file} doesn\'t exist!')
    os.system(f'chmod +x {in_file} && cp {in_file} /opt/pypack/bin/{out_file}')
    pkg_add(f'/opt/pypack/bin/{out_file}',pypack_dir+pypack_packagelst)    # NEED TO ADD THE INSTALLED PACKAGE TO PACKAGE.LST FOR LATER UNINSTALL !!!

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

# def prepend(file, line):                                            # Add line + \n to the begining of a file
    # temp_file='/tmp/pypacktemp-'+get_random_string(20)
    # temp_f=open(temp_file,'w')
    # temp_f.write(line+'\n')
    # with open(file,'r') as f:
        # for l in f.readlines:
            # temp_f.write(l)
    # temp_f.close()
    # os.system(f'mv {temp_file} {file}')

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
def py2elf(imput,output):
    if os.path.isfile('/usr/bin/py2elf'):                           # if py2elf installed
        os.system(f'py2elf -o {output} {imput}') 
    elif os.path.isfile('./py2elf.py'):                                # if py2elf installed
        os.system(f'./py2elf.py -o {output} {imput}')               # if py2elf in same directory
    else:
        exit('py2elf not found')


pypack_dir='/var/lib/pypack/'                                       # Directory where we will have necessary files for pypack to work properly
pypack_packagelst='packages.lst'                                    # File where all stored packages are listed
working_dir=os.popen('pwd').read()[:-1]
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

parser=argparse.ArgumentParser()
parser.add_argument('-i', help='specify name of the package to install (e.g. pypack -i foo -f bar.py will install bar.py and it will be installed in /usr/bin/foo)')
parser.add_argument('-f', help='specify the python3 package to install')
parser.add_argument('-p', '--purge', help='uninstall specified package')
parser.add_argument('-n', '--no-compile', help='if --no-compile is specified, the script will be installed without being compiled',action='count')
args=parser.parse_args()

# PART OF CODE TO INSTALL PACKAGE
# -------------------------------

if args.i and not bool(args.no_compile):                            # Here we do compile the python file to an ELF
    out_file=args.i
    in_file=args.f
    temp_file='/tmp/out'+get_random_string(20)
    if os.path.isfile(f'/usr/bin/{out_file}'):                      # if file exists: exit with error
        exit(f'[error] /usr/bin/{out_file} exists!')
    py2elf(working_dir+'/'+in_file,temp_file)
    os.system(f'chmod +x {temp_file} && sudo mv {temp_file} /usr/bin/{out_file}')
                                                                    # NEED TO ADD THE INSTALLED PACKAGE TO PACKAGE.LST FOR LATER UNINSTALL !!!

if args.i and bool(args.no_compile):                                # Here we don't compile the python file to an ELF
    out_file=args.i
    in_file=args.f
    with open(in_file,'r') as f:
        line1=f.readline()
        if '#!/usr/bin/python' in line1:
            #thats cool
            print(f'{line1} in 1st line. that\'s cool!')
        else:
            #thats not cool
            need2change=1
    if need2change:
        #Let's suppose we use python3
        line_prepender(in_file,'#!/usr/bin/python3')
        #if in_file[-3:] == '.py':
        #    extention=1
    if os.path.isfile(f'/usr/bin/{out_file}'):                      # if file exists: exit with error
        exit('[error] /usr/bin/{out_file} exists!')
    os.system(f'chmod +x {in_file} && cp {in_file} /usr/bin/{out_file}')

# PART OF CODE TO REMOVE PACKAGE
# ------------------------------


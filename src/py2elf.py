#!/usr/bin/python3
import sys
import argparse
import os
import random
import string
if sys.version_info.major != 3:                                     # Check if we're using python 3.X
    exit('[ERROR]: You must be using Python 3.X to run this script')
minor_version=sys.version_info.minor
pypath=f'/usr/include/python3.{minor_version}'
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
arch=os.popen('uname -p').read()                                    # We want to know cpu architecture for compiling
random_temp=get_random_string(20)                                   # We use this variable to make sure some the temporary file we create don't already exist
parser = argparse.ArgumentParser()
parser.add_argument('-o', help='out file')
parser.add_argument('file_to_compile', help='Select python3 file to compile to ELF')
args = parser.parse_args()
in_file=args.file_to_compile
output=args.o
os.system(f'cython3 -3 -o /tmp/{random_temp}.c --embed {in_file}')
os.system(f'gcc -Os -I {pypath} /tmp/{random_temp}.c -o {output} -lpython3.{minor_version} -lpthread -lm -lutil -ldl')
os.system(f'rm /tmp/{random_temp}.c')

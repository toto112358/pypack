#!/usr/bin/python3
import sys
import argparse
import os
import random
import string
if sys.version_info.major != 3:
    exit('[ERROR]: You must be using Python 3.X to run this script')
pypath=f'/usr/include/python3.{sys.version_info.minor}'
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str 
random_temp=get_random_string(20)                                   # We use this variable to make sure some the temporary file we create don't already exist
parser = argparse.ArgumentParser()
parser.add_argument('-o', help='out file')
parser.add_argument('file_to_compile', help='Select python3 file to compile to ELF')
args = parser.parse_args()
in_file=args.file_to_compile
output=args.o
os.system(f'cython3 -o /tmp/{random_temp}.c --embed {in_file}')
os.system(f'gcc -Os -I {pypath} /tmp/{random_temp}.c -o {output} -lpython3.8 -lpthread -lm -lutil -ldl')
os.system(f'rm /tmp/{random_temp}.c')

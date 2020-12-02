#!/usr/bin/python3
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('-o', help='out file')
parser.add_argument('file_to_compile', help='Select python3 file to compile to ELF')
args = parser.parse_args()
in_file=args.file_to_compile
output=args.o
os.system(f'cython3 {in_file} -o {output}_temp.c --embed')
os.system(f'gcc -Os -I /usr/include/python3.8  {output}_temp.c -o {output} -lpython3.8 -lpthread -lm -lutil -ldl')
os.system(f'rm {output}_temp.c')

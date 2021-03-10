#!/usr/bin/python3
import sys
import os
from random import randint


def get_random_string(length):
    return ''.join([chr(randint(97, 122)) for _ in range(length)])


def compile(in_file, out_file, static):
    minor = sys.version_info.minor
    pypath = f'/usr/include/python3.{minor}'
    random_temp = get_random_string(20)

    os.system(f'cython3 -3 -o /tmp/{random_temp}.c --embed {in_file}')
    if static:
        os.system(f'gcc -static -Os -I {pypath} /tmp/{random_temp}.c -o {out_file} -lpython3.{minor} -lpthread -lm -lutil -ldl')
    else:
        os.system(f'gcc -Os -I {pypath} /tmp/{random_temp}.c -o {out_file} -lpython3.{minor} -lpthread -lm -lutil -ldl')
    os.system(f'rm /tmp/{random_temp}.c')


args = sys.argv[1:]
if len(args) == 0:
    print("usage: py2elf [-static, -o (out_file)] in_file")
else:
    in_file=args[-1]
    static = "-static" in args
    out_file = args[args.index("-o")+1] if "-o" in args else "a.out"
    print(in_file)
    compile(in_file, out_file, static)

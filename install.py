#!/usr/bin/python3
import os
in_file='py2elf.py'
output='py2elf'
os.system(f'cython3 {in_file} -o {output}_temp.c --embed')
os.system(f'gcc -Os -I /usr/include/python3.8  {output}_temp.c -o {output} -lpython3.8 -lpthread -lm -lutil -ldl')
os.system(f'rm {output}_temp.c')
os.system('chmod +x py2elf')
os.system('sudo cp py2elf /usr/bin')
print('Successfully installed py2elf (i guess, lazy to check that)')

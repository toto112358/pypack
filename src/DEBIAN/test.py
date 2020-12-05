#!/usr/bin/python3
needle='foo'
with open("test.txt", "r+") as file:
    for line in file:
        if needle in line:
            break
        else: # not found, we are at the eof
            file.write(needle) # append missing data

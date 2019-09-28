#!/usr/bin/env python3
import os.path

DOCUMENTATION = """ cat

concatenate N files together and send to stdout

"""

# get arguments  (everything after the command)
args = sys.argv[1:]

for a in args:
    if os.path.isfile(a):
        with open(a, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                print(line)
    else:
        raise FileNotFoundError("Invalid argument {0}".format(a))

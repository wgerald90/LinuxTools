#!/usr/bin/python3
import sys
import os.path

DOCUMENTATION = """ grep

Given a string and a file find that string in the file
TODO: Given a directory iterate over it searching for the item
returns the file: line number: and the string
"""


def found(item: str, target: str) -> bool:
    return (False, True)[int(item in target)]


# validate the number of arguments passed and assign them
if len(sys.argv[1:]) >= 2:
    item, targets = sys.argv[1], sys.argv[2:]
else:
    print('Invalid number of aruments passed')
    sys.exit(1)
for target in targets:
    if os.path.isfile(target):
        with open(target, 'r') as fp:
            lines = fp.readlines()
            lineNum = 0
            for line in lines:
                lineNum += 1
                if found(item, line):
                    print(f'{target}:{lineNum}:  {line}')
    else:
        print(f'{target} not found')

#!/usr/bin/env python3

import re

def convert(str):
    try:
        int(str)
    except:
        return str
    else:
        return int(str)
def file_listing(filename="src/listing.txt"):
    try:
        re.match()
    except:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        list2 = []
        for line in lines:
            list2.append(tuple(map(convert, line.replace(":", " ").split()[4:])))
    return list2

def main():
    print(file_listing())

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    f = open(filename, "r")
    lines = f.readlines()[1:]
    lines2 = []
    lines3 = []
    for line in lines:
        try:
            lines2.append(re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)$", line).groups())
        except:
            pass
        else:
            pass
    for line in lines2:
        lines3.append(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}")
    return lines3



def main():
    pass

if __name__ == "__main__":
    main()

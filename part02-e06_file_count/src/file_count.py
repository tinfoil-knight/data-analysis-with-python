#!/usr/bin/env python3

import sys

def file_count(filename):
    f = open(filename, "r")
    lines = f.readlines()
    linecnt = len(lines)
    wordcnt = 0
    charcnt = 0
    for line in lines:
        wordcnt = wordcnt + len(line.split())
        charcnt = charcnt + len(line)
    f.close()
    return (linecnt, wordcnt, charcnt)

def main():
    for file in sys.argv[1:]:
        x = file_count(file)
        print(f"{x[0]}\t{x[1]}\t{x[2]}\t{file}")

if __name__ == "__main__":
    main()

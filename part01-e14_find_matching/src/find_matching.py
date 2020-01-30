#!/usr/bin/env python3

def find_matching(L, pattern):
    lst = []
    for i, x in enumerate(L):
        if pattern in x:
            lst.append(i)
    
    return lst


def main():
    pass

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re
def integers_in_brackets(s):
    lst = re.findall(r"\[[\s]*?[]+[+-]?\d*[\s]*\]", s)
    newlst = []
    for i in lst:
        newlst.append(i.strip("[").strip("]").strip(" "))
    return list(map(lambda x : int(x), newlst))

def main():
    pass

if __name__ == "__main__":
    main()

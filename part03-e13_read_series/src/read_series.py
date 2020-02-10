#!/usr/bin/env python3

import pandas as pd

def read_series():
    index = []
    words = []
    while True:
        a = input("Input a line: ")
        if a == "":
            break
        else:
            try:
                index.append(a.split()[0])
                words.append(a.split()[1])
            except:
                print("try again!")
    return pd.Series(words, index=index)


def main():
    print(read_series())

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    b = np.arange(0,n).reshape(1,n)
    c = np.arange(0,n).reshape(n,1)
    return b*c

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()

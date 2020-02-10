#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    rows = np.arange(0,a.shape[0])
    c = a[rows,1] > a[rows,a.shape[1] - 2]
    return a[c]
    
def main():
    pass

if __name__ == "__main__":
    main()

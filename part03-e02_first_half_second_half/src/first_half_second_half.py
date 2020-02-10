#!/usr/bin/env python3

import numpy as np
    
def first_half_second_half(a):
    rows = np.arange(0,a.shape[0])
    print(a)
    m = int(a.shape[1]/2)
    c = np.sum(a[:,:m], axis=1) > np.sum(a[:,m:], axis=1)
    return a[c]



def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2],
                  [5, 8, 2, 3],
                  [1,5, 7, 5]])

if __name__ == "__main__":
    main()

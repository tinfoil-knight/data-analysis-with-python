#!/usr/bin/env python3

import numpy as np

def diamond(n):
    d = []
    for i in range(0, n-1):
        d.append(np.split(np.eye(n, dtype=int),n)[i])
    b = np.eye(n, dtype=int)
    for i in range(n-2, -1, -1):        
        b = np.concatenate((b,d[i]))
    c = []
    for i in range(1, n):
        c.append(np.split(b,n, axis=1)[i])
    for i in range(0,n-1):
        print(b)   
        b = np.concatenate((c[i],b), axis=1)
        

    return b


def main():
    diamond(4)

if __name__ == "__main__":
    main()

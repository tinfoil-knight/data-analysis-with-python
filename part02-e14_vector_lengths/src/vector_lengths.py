#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))

def main():
    print(vector_lengths(np.random.randint(1, 8, (4, 5))))

if __name__ == "__main__":
    main()

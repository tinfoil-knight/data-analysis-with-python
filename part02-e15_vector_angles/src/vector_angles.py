#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    a = np.sum(X*Y, axis=1)
    b = scipy.linalg.norm(X, axis=1) * scipy.linalg.norm(Y, axis=1)
    return 180 /  np.pi * (np.arccos(np.clip(a/b, 0, 1)))
def main():
    print(vector_angles(np.random.randint(1,10, (4,5)), np.random.randint(1,10, (4,5))))

if __name__ == "__main__":
    main()

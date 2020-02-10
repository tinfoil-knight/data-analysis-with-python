#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    print(a)
    if n <= -1:
        return matrix_power(np.linalg.inv(a), abs(n))
    return reduce(lambda x,y : x@y, [a for i in range(n)], np.eye(a.shape[0]))


def main():
    pass


if __name__ == "__main__":
    main()

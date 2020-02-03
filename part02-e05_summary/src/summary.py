#!/usr/bin/env python3

import sys
import math

def keskihajonta(average, numbers):
    a = 0
    for i in numbers:
        a += (i - average) ** 2
    return math.sqrt(a / (len(numbers) - 1))

def summary(filename):
    numbers = []
    
    with open(filename, "r") as f:
        for row in f:
            try:
                numbers.append(float(row))
            except ValueError:
                pass
    
    s = sum(numbers)
    a = s/len(numbers)
    d = keskihajonta(a, numbers)

    return (s,a,d)

def main():
    for f in sys.argv[1:]:
        results = summary(f)
        print(f'File: {f} Sum: {results[0]:.6f} Average: {results[1]:.6f} Stddev: {results[2]:.6f}')

if __name__ == "__main__":
    main()
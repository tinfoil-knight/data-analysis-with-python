#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    return (-b + math.sqrt(b*b - 4*a*c))/(2*a), (-b - math.sqrt(b*b - 4*a*c))/(2*a)


def main():
    solve_quadratic(1,2,3)

if __name__ == "__main__":
    main()

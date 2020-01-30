#!/usr/bin/env python3

def sum_equation(L):
    if len(L) < 1:
        return "0 = 0"
    Ls = [str(x) for x in L]
    s = " + ".join(Ls)
    return  s + f" = {sum(L)}"

def main():
    sum_equation([1,5,7])

if __name__ == "__main__":
    main()

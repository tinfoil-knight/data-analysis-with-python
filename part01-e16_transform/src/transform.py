#!/usr/bin/env python3

def transform(s1, s2):
    L1 = list(map(int, s1.split()))
    L2 = list(map(int, s2.split()))
    L3 = list(zip(L1, L2))
    L4 = [L3[i][0]*L3[i][1] for i in range(len(L3))]
    return L4


def main():
    pass

if __name__ == "__main__":
    main()

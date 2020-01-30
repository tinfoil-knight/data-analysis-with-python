#!/usr/bin/env python3
import numpy as np
def detect_ranges(L):
    Y = np.asarray(sorted(L)).tolist()
    for i in range(len(Y)):
        lst = []
        for j in range(i+1, len(Y)):
            if Y[i:j+1] == [x for x in range(Y[i], Y[j]+1)]:
                lst.append(Y[j])
        
        if len(lst) > 0:
            Y[i] = tuple((Y[i], max(lst)+1))
            Y[i+1:Y.index(max(lst))+1] = []

    return Y




def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

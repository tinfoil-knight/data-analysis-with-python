#!/usr/bin/env python3

import pandas as pd
def create_series(L1, L2):
    if len(L1)!=3 or len(L2)!=3:
        raise Exception
    s1 = pd.Series(L1, index=list("abc"))
    s2 = pd.Series(L2, index=list("abc"))
    return (s1, s2)
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del(s2["b"])
    return (s1, s2)
    
def main():
    srs = create_series([1,2,3], [4,5,6])
    modified = modify_series(srs[0], srs[1])
    modified[0] + modified[1]
    
if __name__ == "__main__":
    main()

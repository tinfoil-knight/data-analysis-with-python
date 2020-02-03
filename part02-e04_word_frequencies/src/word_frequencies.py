#!/usr/bin/env python3
import re
def word_frequencies(filename="src/alice.txt"):
    d = {}
    with open(filename, "r") as f:
        for row in f:
            r = list(row.split())
            for w in r:
                w = w.strip("""!"#$%&'()*,-./:;?@[]_""")
                if w in d.keys():
                    d[w] = d[w] + 1
                else:
                    d[w] = 1

    return d
    
def main():
    word_frequencies()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def reverse_dictionary(d):
    D = {}
    for key, value in d.items():
        for val in value:
            try:
                if D[val]:
                    pass
            except:
                D[val] = [key]
            else:
                D[val].append(key)
                
    return D

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()

# reverse_dictionary(d)
# {'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}
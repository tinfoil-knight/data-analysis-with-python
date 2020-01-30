#!/usr/bin/env python3

def interleave(*lists):
    
    return list(zip(*lists))
    # for i in range(len(lists[0])):
    #     for x in lists:
    #         somelist.append(x[i])
    
    # return somelist

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

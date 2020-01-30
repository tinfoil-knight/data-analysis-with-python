#!/usr/bin/env python3

def triple(a):
    return a*3

def square(a):
    return a*a

def main():
    for i in range(1,11):
        x = triple(i)
        y = square(i)
        if x < y:
            break
        print(f"triple({i})=={x} square({i})=={y}")


if __name__ == "__main__":
    main()

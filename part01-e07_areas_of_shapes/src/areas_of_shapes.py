#!/usr/bin/env python3

import math

def circle(r):
    return math.pi * r * r

def rectangle(w, h):
    return w * h

def triangle(b, h):
    return (b * h)/2

def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if len(shape) == 0:
            break
        elif shape == "triangle":
            b = int(input("Give base of the triangle: "))
            h = int(input("Give height of the triangle: "))
            print(f"The area is {triangle(b, h)}")
        elif shape == "rectangle":
            w = int(input("Give width of the rectangle: "))
            h = int(input("Give height of the rectangle: "))
            print(f"The area is {rectangle(w, h)}")
        elif shape == "circle":
            r = int(input("Give radius of the circle: "))
            print(f"The area is {circle(r)}")
        else:
            print("Unknown shape!")



if __name__ == "__main__":
    main()

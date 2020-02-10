#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# Not you K, not you
def to_grayscale(image):
    return np.dot(image[...,:3], [0.2126, 0.7152, 0.0722])

def to_red(image):
    return image.copy() * np.array([1,0,0])

def to_green(image):
    return image.copy() * np.array([0,1,0])

def to_blue(image):
    return image.copy() * np.array([0,0,1])

def main():

    image = plt.imread("src/painting.png")
    gray = to_grayscale(image)
    plt.imshow(gray, cmap="gray")
    plt.show()

    r = to_red(image)
    g = to_green(image)
    b = to_blue(image)

    plt.subplot(3,1,1)
    plt.imshow(r)
    plt.subplot(3,1,2)
    plt.imshow(g)
    plt.subplot(3,1,3)
    plt.imshow(b)
    plt.show()

if __name__ == "__main__":
    main()
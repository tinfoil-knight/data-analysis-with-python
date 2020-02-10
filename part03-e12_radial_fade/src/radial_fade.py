#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    h, w = a.shape[:2]
    y = (h-1)/2
    x = (w-1)/2
    return y,x

def radial_distance(a):
    tupA = a.shape[:2]
    y, x = center(a)
    return np.array([[ np.sqrt((j-y)**2+(i-x)**2) for i in range(tupA[1]) ] for j in range(tupA[0])])   

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    # Crap Code Starts
    if a.shape[:2][0]*a.shape[:2][1] == 1:
        return np.array([1]).reshape(1,1)
    if np.count_nonzero(a) == 0:
        arr = (1 - scale(radial_distance(a)))
        h, w = arr.shape[:2]
        y = (h-1)//2
        x = (w-1)//2
        arr[y,x] = 1.0
        return arr
    # Crap Code Ends
        
    return (1 - scale(radial_distance(a)))

def radial_fade(a):
    h, w = a.shape[:2]
    y = (h-1)//2
    x = (w-1)//2
    # Crap Code Starts
    if h*w < 101:
        arr = a * radial_mask(a).reshape(h,w,1)
        arr[y,x] = a[y,x]
        return arr
    # Crap Code Ends
    return a * radial_mask(a).reshape(h,w,1)

def main():
    painting = plt.imread("src/painting.png")
    masked = radial_mask(painting.copy())
    faded = radial_fade(painting.copy())
    
    plt.subplot(3,1,1)
    plt.imshow(painting)
    plt.subplot(3,1,2)
    plt.imshow(masked)
    plt.subplot(3,1,3)
    plt.imshow(faded)
    plt.show()
    

if __name__ == "__main__":
    main()
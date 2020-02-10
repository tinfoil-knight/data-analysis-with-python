#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
def main():
    ax = np.array([2,4,6,7])
    ay = np.array([4,3,5,1])
    bx = np.array([1,2,3,4])
    by = np.array([4,2,3,1])
    plt.plot(ax, ay)
    plt.plot(bx, by)
    plt.title("title")  
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()   

if __name__ == "__main__":
    main()

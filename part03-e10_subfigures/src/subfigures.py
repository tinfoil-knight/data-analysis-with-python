#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    plt.subplot(1,2,1)
    graphX = a[:,0]
    graphY = a[:,1]
    plt.plot(graphX,graphY)
    plt.subplot(1,2,2)
    scatterX = a[:,0]
    scatterY = a[:,1]
    plt.scatter(scatterX, scatterY, c=a[:,2], s=a[:,3])
    plt.show()

def main():
    arr = np.random.randint(1,10, (4,4))
    subfigures(arr)

if __name__ == "__main__":
    main()

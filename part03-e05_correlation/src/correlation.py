#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = np.array(load())
    return scipy.stats.pearsonr(data[:,0], data[:,2])[0]

def correlations():
    data = load()
    col_0 = np.array(data[:, 0])
    col_1 = np.array(data[:, 1])
    col_2 = np.array(data[:, 2])
    col_3 = np.array(data[:, 3])

    cor_data = np.array([col_0, col_1, col_2, col_3])
    return np.corrcoef(cor_data)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()

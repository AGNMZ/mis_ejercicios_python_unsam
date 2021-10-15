# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:10:56 2021

@author: amene
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.show()
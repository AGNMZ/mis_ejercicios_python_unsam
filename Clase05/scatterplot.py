# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:13:15 2021

@author: amene
"""
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
colors = colors + 250
area = (30 * np.random.rand(N))**2
  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.3)
plt.show()
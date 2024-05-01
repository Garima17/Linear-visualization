#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:05:24 2024

@author: garimajindal
"""

import matplotlib.pyplot as plt

# Data
data = [
    [7.7, 2, 5.05, 3.34, 3.81, 2, 4.18, 5.26, 5.91],
    [2,1.58,2,1.86,3.4,4,3.9,3.36,2],
    [8.53,24.1,18.61,27.98,13.42,10.53,9.14,8.66,17.23],
    [33.1,14.91,30.9,20.4,20,8.15,20.01,5.9,10.56],
    [18.61,5.19,13.64,13.72,5,8.7,9.01,4.89,4.33],
    [8.2,11.54,5.42,11.8,7.4,5.45,5.61,11.47,12.94],
    [12.51,33.86,24.01,9.76,15.75,10.92,3.14,3,3.19],
    [7.9,1.46,7.21,2,3,2.4,3.7,4.02,8.09],
    [39.46,11.82,24.4,4.41,10.08,5.5,5.46,4.5,3.89],
    [3,5.6,18.55,13.75,6.13,11,6.8,16.39,10.7]

]

# Box plot
plt.figure(figsize=(10, 7))
plt.boxplot(data, patch_artist=True)

# Add labels
plt.xticks([i+1 for i in range(len(data))],
           ['Count Communities', 'Find Community', 'Largest Community', 'Smallest Community', 'Size Ranking',
            'Compare Community size', 'Densest community', 'Low density communities', 'Density Ranking',
            'Compare Density'], rotation=45, ha='right')
plt.ylabel('seconds')

# Show plot
plt.title('Box Plots')
plt.tight_layout()
plt.show()
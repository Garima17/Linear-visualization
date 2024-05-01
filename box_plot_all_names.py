#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:27:37 2024

@author: garimajindal
"""

import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Count Communities': [7.78, 2, 5.05, 3.34, 3.81, 2, 4.18, 5.26, 5.91],
    'Find Community': [2, 1.58, 2, 1.86, 3.4, 4, 3.9, 3.36, 2],
    'Largest Community': [8.53, 24.1, 18.61, 27.98, 13.42, 10.53, 9.14, 8.66, 17.23],
    'Smallest Community': [33.1, 14.91, 30.9, 20.4, 20, 8.15, 20.01, 5.9, 10.56],
    'Size Ranking': [18.61, 5.19, 13.64, 13.72, 5, 8.7, 9.01, 4.89, 4.33],
    'Compare Community size': [8.2, 11.54, 5.42, 11.8, 7.4, 5.45, 5.61, 11.47, 12.94],
    'Densest community': [12.51, 33.86, 24.01, 9.76, 15.75, 10.92, 3.14, 3, 3.19],
    'Low density communities': [7.9, 1.46, 7.21, 2, 3, 2.4, 3.7, 4.02, 8.09],
    'Density Ranking': [39.46, 11.82, 24.4, 4.41, 10.08, 5.5, 5.46, 4.5, 3.89],
    'Compare Density':[3,5.6,18.55,13.75,6.13,11,6.8,16.39,10.7,],    
    'Node Connections': [4.6, 10.36, 3.79, 10.01, 6.9, 4, 10.83, 10.5, 3],
    'Most Connected': [7.69, 20.47, 30.86, 22.56, 21.97, 19.99, 11.9, 8.1, 6],
    'Least Connected': [10.37, 1.64, 9.32, 8.07, 3.2, 7.33, 11.65, 3.33, 3.39],
    'Community Connection Raking': [54, 4.9, 31, 14, 15, 2.85, 30.58, 3.43, 3.79],
    'Find Connection': [5.8, 8.7, 10.81, 15.14, 15.14, 7.33, 7.67, 7.33, 6.7],
    'Compare Community Connections': [12.65, 8.9, 6.47, 13.74, 8.45, 7, 8.9, 7.45, 12.37],
    'Count Adjacent Communities': [10.65, 5.17, 10.04, 14.24, 3.51, 7.1, 4.2, 3.23, 2.34],
    'Strength of Connections': [74.14, 25.7, 53.7, 79.87, 60.06, 59.06, 90, 10.45, 79.22],
    'Most Central Node': [26.41, 42.73, 27.5, 46.46, 36.38, 24.28, 36, 15.77, 43.33],
    'Least Central Node': [22.74, 4.83, 7.96, 18.07, 29.07, 12.37, 17.79, 9.18, 36.39]
}

# Create DataFrame
df = pd.DataFrame(data)

# Box plot
plt.figure(figsize=(16, 8))
df.boxplot(rot=45, patch_artist=True)
plt.title('Box Plot for Network Metrics')
plt.ylabel('Time(Sec)')
plt.tight_layout()
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:20:55 2024

@author: garimajindal
"""

import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Node Connections': [4.6, 10.36, 3.79, 10.01, 6.9, 4, 10.83, 10.5, 3],
    'Most Connected': [7.69, 20.47, 30.86, 22.56, 21.97, 19.99, 11.9, 8.1, 6],
    'Least Connected': [10.37, 1.64, 9.32, 8.07, 3.2, 7.33, 11.65, 3.33, 3.39],
    'Community Connection Raking': [54, 4.9, 31, 14, 15, 2.85, 30.58, 3.43, 3.79],
    'Find Connection': [5.8, 8.7, 10.81, 15.14, 15.14, 7.33, 7.67, 7.33, 6.7],
    'Compare Community Connections': [12.65, 8.9, 6.47, 13.74, 8.45, 7, 8.9, 7.45, 12.37],
    'Count Adjacent Communities': [10.65, 5.17, 10.04, 14.24, 3.51, 7.1, 4.2, 3.23, 2.34],
    'Strength of Connections': [74.14, 25.7, 53.7, 79.87, 60.06, 59.06, 120, 10.45, 79.22],
    'Most Central Node': [26.41, 42.73, 27.5, 46.46, 36.38, 24.28, 36, 15.77, 43.33],
    'Least Central Node': [22.74, 4.83, 7.96, 18.07, 29.07, 12.37, 17.79, 9.18, 36.39]
}

# Create DataFrame
df = pd.DataFrame(data)

# Box plot
plt.figure(figsize=(12, 6))
df.boxplot(rot=45, patch_artist=True)
plt.title('Box Plot for Network Metrics')
plt.ylabel('Values')
plt.tight_layout()
plt.show()
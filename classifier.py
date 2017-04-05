from sklearn import tree
import numpy as np
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import math

## 1. Read in the data line by line and put it into a matrix
import csv

def list_creator(file):
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
    return data

inhib_file = open('in.csv', 'r')
data = list_creator(inhib_file)
data = np.array(data)
inhib_data = data.astype(int)

## 2. Normalize this data
def normalize(list):
    normalized_list = []
    for row in list:
        normalized = row / np.linalg.norm(row)
        normalized_list.append(normalized)
    return normalized_list

normalized_inhib = normalize(inhib_data)

## 3. Curve smoothing
def smooth_points(list, x, x_smooth):
    smoothed_list = []
    for row in list:
        y_smooth = spline(x,row,x_smooth)
        smoothed_list.append(y_smooth)
    return smoothed_list

x = np.array(range(-50,51))
x_smooth = np.linspace(x.min(), x.max(), num=1000)
smoothed_inhib = smooth_points(normalized_inhib, x, x_smooth)

## 4. Machine learning aspect
## For now, we are going to use a decision tree implementation of machine learning.

## First, we need features. These will essentially be our data (TODO: use the normalized or smoothed points? using the normalized for now).
shanks_file = open('shanks.csv', 'r')
shanks_dat = list_creator(shanks_file)
shanks_dat = np.array(shanks_dat)
shanks_dat = shanks_dat.astype(int)

## Decide if same shank or not - this will be one of the aspects of our feature.
def is_same_shank(list):
    same_shank = []
    for row in list:
        if row[2] == row[3]:
            same_shank.append(1)
        else:
            same_shank.append(0)
    return same_shank

same_shank_list = is_same_shank(shanks_dat)

## Each observation should go with a 1 or a 0 - that is, whether or not that observation had a same shank.
def put_into_2d_list(inhib,shank):
    features = []
    for i in inhib:
        for j in shank:
            features.append([j,i])
    return features

features = put_into_2d_list(normalized_inhib, same_shank_list)

## Next, we need labels. This tells our algorithim what response to associate with an associating feature.
labels = []
length = int(math.sqrt(len(features)))
for i in range(length):
    print features[i][1]
    if features[i][0] == 1:
        # same shank, check if low at 0
        if features[i][1][50] == 0:
            # low at 0, check for recovery
            continue
        else:
            # not low at 0, low elsewhere?
            continue
    else:
        # not same shank, still need to check for low bin
        if features[i][1][49] == 0:
            # still has a low bin
            continue
        else:
            # no low bin
            labels.append("NI")
print labels
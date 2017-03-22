from sklearn import tree
import numpy as np
from scipy.interpolate import spline
import matplotlib.pyplot as plt

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


## For now, we are going to use a decision tree implementation of machine learning.

## First, we need features. These will essentially be our data.

## Next, we need labels. This tells our algorithim what response to associate with an associating feature.


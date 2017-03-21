from sklearn import tree
import numpy as np
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
## TODO: curve smoothing - look into convolusion


## For now, we are going to use a decision tree implementation of machine learning.

## First, we need features. These will essentially be our data.

## Next, we need labels. This tells our algorithim what response to associate with an associating feature.


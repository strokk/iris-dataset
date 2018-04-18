# Project 2018 - Programming and Scripting
# Guilherme G. C. Paes - 2018

# After some research I've found out that for the purpose of this project numpy and pandas would be the best libraries to use
# Importing the libraries:
import numpy as np
import pandas as pd

# Importing the dataset from iris.csv file
iris = pd.read_csv("iris.csv")
#Printing some data just for visualization
print(iris.head())

# Printing the rows and columns of the data using the shape property:
print(iris.shape)

#Calculating the mean of each column using numpy
print(np.mean(iris))

#Calculating the max of each column using numpy
print(np.max(iris))

#Calculating the min of each column using numpy
print(np.min(iris))

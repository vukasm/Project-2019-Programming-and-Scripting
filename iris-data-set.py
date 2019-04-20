#Margarita Vukas, 2019-04-06
#Iris Data set

#Import all the modules and functions.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

#Load Iris-data-set.csv into Pandas dataFrame.

iris=pd.read_csv("iris-data-set.csv")

#After loading the data via pandas, I check what the content is, using head and tail commands.
head=iris.head() #to check the first 10 rows of the data set
tail=iris.tail() #to check the last 10 rows of the data set

print("First 10 lines of data set:")
print(head)
print("Last 10 lines od data set:")
print(tail)

time.sleep(5)

#This function shows the shape of the data set(Number of rows and columns).
print("Whats is the shape of this data set?")
print(iris.shape)

time.sleep(5)

#This function shows the names of the data set's columns.
print("What are the names of this data set's columns?")
print(iris.columns)

time.sleep(5)

#This function shows how many observations for each class label are present (How many flowers for each species are present).
print("How many flowers for each species are present?")
print(iris["species"].value_counts())

time.sleep(5)

#This function shortly describes the data set.
print("This is the short description of the data set:")
print(iris.describe())

time.sleep(5)

#This function calculates the mean of each variable given in the data set.
print("The mean of the each variable is:")
print(iris.mean())

time.sleep(5)

#Now, I visualise the data; first with a boxplot.
#Adapted from: https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
plt.figure(figsize = (10, 7)) #Determining the size of the plot
plt.ylabel('length in cm') #Labeling y axis
plt.title('Iris Data Set Boxplot') #Giving a title to the plot
iris.boxplot() #Boxplot command
plt.show()
plt.close()




#Next, histograms.
#Histograms are representations of the univariate plots for each measurement.

iris.hist() #Histogram command

plt.show()
plt.close()

#Next, looking at interactions between variables.
#Scatterplots of all pairs of attributes
#Pairwise scatter plot: Pair-Plot

sns.set_style("whitegrid") #Setting seaborn theme to whitegrid.
sns.pairplot(iris, hue="species", height=3,) #Pairplot command
plt.show()  

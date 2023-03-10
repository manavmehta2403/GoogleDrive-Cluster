#importing all the essential libraries 
import pandas as pd #to read the csv file 
import numpy as np #although this is optional for this question
import matplotlib.pyplot as plt #to draw the grap

#using pandas to read the csv file and stroing in the dataframe df

'''Although it is not nesscery to pass sep (seperator) argument as delimitor'''
df = pd.read_csv("messy_data.csv", sep = ",") #in double quotes please keep the file path

print(df) # to print the entire dataframe 

print("-----------------------------------------------------------------------")
#printing the first five rows of the dataframe=>dataframe.head()=> pass the number by default it is 5
print(df.head())



print("-----------------------------------------------------------------------")
print("DF info\n")
# dataframe=>size returns number of rows X columns
size = df.size 
  
# dataframe=>shape returns the tuple of shape in (rows, columns)
shape = df.shape 
  
# dataframe=>ndim returns the dimension 1 for 1D and 2 for 2D
dimension = df.ndim

#printing the size, shape and dimension of the dataframe
print("Size =",size,"\nShape =",shape,"\nDimension =",dimension)



print("-----------------------------------------------------------------------")
print("Columns info\n")
#dataframe=>dtype returns the datatype of the dataframe
print(df.dtypes)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#print all the information about the column use .info()
print(df.info())



print("-----------------------------------------------------------------------")
print("Stats\n")
#printing out the statistics of dataframe=>dataframe.describe()
print(df.describe())


'''NaN values are the missing values (in technical  terms null values) in the dataframe
They should not be confused with the 0 (zero), as zero is a value in the dataframe.

For example consider this dataframe:-
|col1|
------
|23  |
------
|24  |
------
|0   |  => zero value
------
|NaN |  => null value
------
'''

#to remove all the NaN values from the dataframe =>.dropna()
df = df.dropna()
print("-----------------------------------------------------------------------")
print(df.head())

'''NOTE (by default, inplace is False
there is one parameter call inplace this can only take boolean values
True => if inplace = True then data is renamed as new data, basically replcaes the dataframe after the opertions
False => if inplace = False then data is displayed as copied dataframe, basically makes the new copy dataframe after the opertions'''


# gca stands for 'get current axis'
ax = plt.gca()  #it is used to print the graph on the same cartesian plane

#plot the scatter graph where x-axis is eplison (index) and y-axis are aplha,beta,gamma and delta
df.plot(kind='scatter',x='epsilon',y='alpha',color='red', ax=ax)
df.plot(kind='scatter',x='epsilon',y='beta', color='blue', ax=ax)
df.plot(kind='scatter',x='epsilon',y='gamma', color='green', ax=ax)
df.plot(kind='scatter',x='epsilon',y='delta', color='orange',ax=ax)

# Add title and axis names
plt.title('Data')
plt.xlabel('Epsilon')
plt.ylabel('Particles')


#display the graph
plt.show()

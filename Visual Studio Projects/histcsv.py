import pandas as pd              #This is used to load .csv and perform analysis on the data
import matplotlib.pyplot as plt  #This is used for plotting

x=input("Please enter:\n 1 for PopChange.csv\n 2 for Housing.csv\n\n ")

#POPCHANGE:
if x==1:
   popchange=pd.read_csv("PopChange.csv") #loading .csv file into the dataframe(popchange)
   popchange_selected = popchange[["Pop Apr 1","Pop Jul 1", "Change Pop"]] #Only the #selected columns is stored in popchange_selected
   popchange_selected.hist(bins=50, figsize=(20,15)) 
   plt.show() #Displays histogram of all the selected columns 
   print(popchange_selected.describe())#Describe method from pandas library is used to #calculate Count, Mean, Standard Deviation, Min, Max

#HOUSING:
if x==2:
   housing=pd.read_csv("Housing.csv")
   housing_selected=housing[["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"]] #Only the #selected columns is stored in housing_selected
   #if there are extra columns after "UTILITY" that are to be considered for analysis,
   #use the following line instead of the above line
   #housing_selected=housing.iloc[:,4:]
   housing_selected.hist(bins=50, figsize=(20,15))
   plt.show() #Displays histogram of all the selected columns 
   print(housing_slected.describe())#Describe method from pandas library is used to #calculate Count, Mean, Standard Deviation, Min, Max

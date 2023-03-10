#import statements

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

import math

# fixing random state for reproducibility

##np.random.seed(214801)
##
##mu, sigma = 100, 15
##
##x = mu + sigma * np.random.randn(10000)
##
### the histogram of hte data
##
##n, bins, patches = plt.hist (x, 20, density=True, facecolor='b', alpha =0.75)
##
##plt.grid(True)
##
###Assign to a figure
##
##fig1=plt
##
### Save Figure for Download
##
##fig1.savefig('display5.svg')

##read the files: as the data frames
pop_df = pd.read_csv("PopChnage.csv")#reading the  pop change csv
hs_df = pd.read_csv("Housing.csv") #reading the housing csv

def menu(): # display the menu

   """print a menu for the user to use in the data analysis application"""

   print('\nSelect the file you want to analyze: ')

   print('1: Population Data ')

   print('2: Housing Data ')

   print('3: Exit the application')

   

def pop_data_column(): # display options for population data

   """print the menu for the user to use in the pop data column"""

   print('\nYou have entered Population Data ')

   print('\nSelect the Column you want to analyze: ')

   print('a: Pop Apr 1 ')

   print('b: Pop Jul 1 ')

   print('c: Change Pop')

   print('d: Exit Column')

def pop_Apr_1(): # display Pop Apr 1 statistics

   """print the menu for the user to use in the pop data column"""

   print('\nYou have selected Pop Apr 1')

   print('\nThe statistics for this column are: ')

   print('Count = ',pop_df["Pop Apr 1"].count())

   print('Mean = ',pop_df["Pop Apr 1"].mean())

   print('Standard Deviation = ',pop_df["Pop Apr 1"].std())

   print('Max = ',pop_df["Pop Apr 1"].max())
   
   n, bins, patches = plt.hist (pop_df["Pop Apr 1"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('pop_Apr_1.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   

def pop_Jul_1(): # display Pop Jul 1 statistics

   """print the menu for the user to use in the pop data column"""

   print('\nYou have selected Pop Jul 1')

   print('\nThe statistics for this column are: ')

   print('Count = ',pop_df["Pop Jul 1"].count())

   print('Mean = ',pop_df["Pop Jul 1"].mean())

   print('Standard Deviation = ',pop_df["Pop Jul 1"].std())

   print('Max = ',pop_df["Pop Jul 1"].max())

   n, bins, patches = plt.hist (pop_df["Pop Jul 1"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('pop_Jul_1.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   

def change_pop(): # display change_pop statistics

   """print the menu for the user to use in the change pop column"""

   print('\nYou have selected Change Pop')

   print('\nThe statistics for this column are: ')

   print('Count = ',pop_df["Change Pop"].count())

   print('Mean = ',pop_df["Change Pop"].mean())

   print('Standard Deviation = ',pop_df["Change Pop"].std())

   print('Max = ',pop_df["Change Pop"].max())
   
   n, bins, patches = plt.hist (pop_df["Change Pop"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('change_pop.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')


   
def exit_column(): # exit the column
   """Bring user back to main menu"""
   menu()


   
def housing_data(): # display options for housing data

   """print the menu for the user to use in the pop data column"""

   print('\nYou have entered Population Data ')

   print('\nSelect the Column you want to analyze: ')

   print('a: Age ')

   print('b: Bedrooms ')

   print('c: Built')

   print('d: N Units')

   print('e: Rooms')

   print('f: Weight')

   print('g: Utility')

   print('h: Exit Column')

def age(): # display age statistics

   """print the menu for the user to use in the age column"""

   print('\nYou have selected Age')

   print('\nThe statistics for this column are:')

   print('Count = ',hs_df["AGE"].count())

   print('Mean = ',hs_df["AGE"].mean())

   print('Standard Deviation = ',hs_df["AGE"].std())

   print('Max = ',hs_df["AGE"].max())

   n, bins, patches = plt.hist (hs_df["AGE"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('age.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')
   
   #housing_data()

   

def bedrooms(): # display bedroom statistics

   """print the menu for the user to use in the Bedrooms column"""

   print('\nYou have selected Bedrooms')

   print('\nThe statistics for this column are:')

   print('Count = ',hs_df["BEDRMS"].count())

   print('Mean = ',hs_df["BEDRMS"].mean())

   print('Standard Deviation = ',hs_df["BEDRMS"].std())

   print('Max = ',hs_df["BEDRMS"].max())

   n, bins, patches = plt.hist (hs_df["BEDRMS"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('bedrooms.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   #housing_data()

def built(): # display built statistics

   """print the menu for the user to use in the Bedrooms column"""

   print('\nYou have selected Bedrooms')

   print('\nThe statistics for this column are:')

   print('Count = ',hs_df["BUILT"].count())

   print('Mean = ',hs_df["BUILT"].mean())

   print('Standard Deviation = ',hs_df["BUILT"].std())

   print('Max = ',hs_df["BUILT"].max())
   
   n, bins, patches = plt.hist (hs_df["BUILT"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('built')
   
   print('**** The Histogram of this column can be downloaded now ****')

   #housing_data()

def n_units(): # display NUnits statistics

   """print the menu for the user to use in the NUnits column"""

   print('\nYou have selected NUnits')

   print('\nThe statistics for this column are:')

   print('Count = ',hs_df["NUNITS"].count())

   print('Mean = ',hs_df["NUNITS"].mean())

   print('Standard Deviation = ',hs_df["NUNITS"].std())

   print('Max = ',hs_df["NUNITS"].max())
   
   n, bins, patches = plt.hist (hs_df["NUNITS"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('n_units.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   #housing_data()

def rooms(): # display Rooms statistics

   """print the menu for the user to use in the Rooms column"""

   print('\nYou have selected Rooms')

   print('\nThe statistics for this column are:')

   print('Count = ',hs_df["ROOMS"].count())

   print('Mean = ',hs_df["ROOMS"].mean())

   print('Standard Deviation = ',hs_df["ROOMS"].std())

   print('Max = ',hs_df["ROOMS"].max())

   n, bins, patches = plt.hist (hs_df["ROOMS"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('rooms.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   #housing_data()

def weight(): # display Weight statistics

   """print the menu for the user to use in the Weight column"""

   print('\nYou have selected Weight')

   print('\nThe statistics for this column are:')

   print('Count =  ',hs_df["WEIGHT"].count())

   print('Mean = ',hs_df["WEIGHT"].mean())

   print('Standard Deviation = ',hs_df["WEIGHT"].std())

   print('Max = ',hs_df["WEIGHT"].max())

   n, bins, patches = plt.hist (hs_df["WEIGHT"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('weight.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   #housing_data()

def utility(): # display Utility statistics

   """print the menu for the user to use in the Utility column"""

   print('\nYou have selected Utility')

   print('\nThe statistics for this column are:')

   print('Count = ',hs_df["UTILITY"].count())

   print('Mean = ',hs_df["UTILITY"].mean())

   print('Standard Deviation = ',hs_df["UTILITY"].std())

   print('Max = ',hs_df["UTILITY"].max())

   n, bins, patches = plt.hist (hs_df["UTILITY"], 20, density=True, facecolor='b',alpha =0.75)
   plt.grid(True)
   plt.show()
   fig = plt
   fig.savefig('utility.svg')
   
   print('**** The Histogram of this column can be downloaded now ****')

   #housing_data()

   

print('**** Welcome to the Python Data Analysis Application ****')

while True:

   menu()

   SELECTION = input('Please enter your choice: ')#Prompt user for input

   if SELECTION == '1':#check if option 1 is selected

       pop_data_column()

       USER_CHOICE = input('Please make your choice: ') #Prompt user for input

       if USER_CHOICE == 'A' or USER_CHOICE == 'a':

           pop_Apr_1()

       elif USER_CHOICE == 'B' or USER_CHOICE == 'b':

           pop_Jul_1()

       elif USER_CHOICE == 'C' or USER_CHOICE == 'c':

           change_pop()

       elif USER_CHOICE == 'D' or USER_CHOICE == 'd':

           exit_column()

           break

       else:

           print('Please enter a, b, c, or d.')

           pop_data_column()

   elif SELECTION == '2':#Check if the user is choosing option 2

       housing_data()

       USER_CHOICE = input('Please make your choice: ') #Prompt user for input

       if USER_CHOICE == 'A' or USER_CHOICE == 'a':

           age()

       elif USER_CHOICE == 'B' or USER_CHOICE == 'b':

           bedrooms()

       elif USER_CHOICE == 'C' or USER_CHOICE == 'c':

           built()

       elif USER_CHOICE == 'D' or USER_CHOICE == 'd':

           n_units()

       elif USER_CHOICE == 'E' or USER_CHOICE == 'e':

           rooms()

       elif USER_CHOICE == 'F' or USER_CHOICE == 'f':

           weight()

       elif USER_CHOICE == 'G' or USER_CHOICE == 'g':

           utility()

       elif USER_CHOICE == 'h' or USER_CHOICE == 'h':

           exit_column()

           break

       else:

           print('Please enter a, b, c, d, e, f, g, or h.')

           housing_data()

   elif SELECTION == '3':#check for selection to be the exit option

       print('You selected 3.')

       print('Thanks for using the Data Analysis Application')

       print('**************************************************************')

       break

   #invalid menu

   else:

       print('Invalid input, please try again')

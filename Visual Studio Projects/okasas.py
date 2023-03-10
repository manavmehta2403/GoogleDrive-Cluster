#import statements

import numpy as np

import matplotlib.pyplot as plt

import pandas

import math

# fixing random state for reproducibility

np.random.seed(214801)

mu, sigma = 100, 15

x = mu + sigma * np.random.randn(10000)

# the histogram of hte data

n, bins, patches = plt.hist (x, 20, density=True, facecoloer='b', alpha =0.75)

plt.grid(TRUE

#Assign to a figure

fig1=plt

# Save Figure for Download

fig1.savefig('display5.svg')

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

def pop_apr_1(): # display Pop Apr 1 statistics

   """print the menu for the user to use in the pop data column"""

   print('\nYou have selected Pop Apr 1')

   print('\nThe statistics for this column are: ')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   

def pop_Jul_1(): # display Pop Jul 1 statistics

   """print the menu for the user to use in the pop data column"""

   print('\nYou have selected Pop Jul 1')

   print('\nThe statistics for this column are: ')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   

def change_pop(): # display change_pop statistics

   """print the menu for the user to use in the change pop column"""

   print('\nYou have selected Change Pop')

   print('\nThe statistics for this column are: ')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

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

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

   

def bedrooms(): # display bedroom statistics

   """print the menu for the user to use in the Bedrooms column"""

   print('\nYou have selected Bedrooms')

   print('\nThe statistics for this column are:')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

def built(): # display built statistics

   """print the menu for the user to use in the Bedrooms column"""

   print('\nYou have selected Bedrooms')

   print('\nThe statistics for this column are:')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

def n_units(): # display NUnits statistics

   """print the menu for the user to use in the NUnits column"""

   print('\nYou have selected NUnits')

   print('\nThe statistics for this column are:')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

def Rooms(): # display Rooms statistics

   """print the menu for the user to use in the Rooms column"""

   print('\nYou have selected Rooms')

   print('\nThe statistics for this column are:')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

def Weight(): # display Weight statistics

   """print the menu for the user to use in the Weight column"""

   print('\nYou have selected Weight')

   print('\nThe statistics for this column are:')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

def Utility(): # display Utility statistics

   """print the menu for the user to use in the Utility column"""

   print('\nYou have selected Utility')

   print('\nThe statistics for this column are:')

   print('Count = ?????? ')

   print('Mean = ?????? ')

   print('Standard Deviation = ?????')

   print('Max = ???????')

   print('**** The Histogram of this column can be downloaded now ****')

   housing_data()

   

print('**** Welcome to the Python Data Analysis Application ****')

while True:

   menu()

   SELECTION = input('Please enter your choice: ')#Prompt user for input

   if SELECTION == '1':#check if option 1 is selected

       pop_data_column()

       USER_CHOICE = input('Please make your choice') #Prompt user for input

       if USER_CHOICE == 'A' or USER_CHOICE == 'a':

           pop_apr_1()

       elif USER_CHOICE == 'B' or USER_CHOICE == 'b':

           pop_Jul_1

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

       USER_CHOICE = input('Please make your choice') #Prompt user for input

       if USER_CHOICE == 'A' or USER_CHOICE == 'a':

           age()

       elif USER_CHOICE == 'B' or USER_CHOICE == 'b':

           bedrooms()

       elif USER_CHOICE == 'C' or USER_CHOICE == 'c':

           built()

       elif USER_CHOICE == 'D' or USER_CHOICE == 'd':

           n_units()

       elif USER_CHOICE == 'E' or USER_CHOICE == 'e':

           Rooms()

       elif USER_CHOICE == 'F' or USER_CHOICE == 'f':

           Weight()

       elif USER_CHOICE == 'G' or USER_CHOICE == 'g':

           Utility()

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

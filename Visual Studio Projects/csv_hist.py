'''IN CASE YOU WANT SPECIFIC STATS COUNT, MEAN, STD, MAX, MIN
USE THEIR METHOD INDIVIDUAL OTHERWISE USE DESCRIBE METHOD'''
#calling all the essential libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating the function for the menu
def menu():
    #displaying the result
    print("""Select the file you want to analyze:
            1. Population Data
            2. Housing Data
            3. Exit the Program""")

    #to avoid any traceback
    try:
        #taking the user input
        selection = int(input("Enter the option you want to analyze: "))
        ##cheching whether the user input in the specific range
        if (1 <= selection <= 3):
            pass
        else:
            print("\nPlease enter the correct option\n")
            menu() #calling recurssively the options
            
    #catch the try block
    except:
        print("\nPlease enter the correct option\n")
        menu()# calling the recursive way for menu if try dont execute

    if (selection == 3):
        print('Thanks for using the Data Analysis Application')
        print('**************************************************************')
        quit()
    
    return selection


def operations(selection):

    #taking col_choice variable to to select the column
    col_choice = ""
    
    #performing the operation for the selection 1
    if (selection == 1):
        pop_df = pd.read_csv("PopChnage.csv")

        #printing column menu
        print("""Select the Column you want to analyze:
                a. Pop Apr 1
                b. Pop Jul 1
                c. Change Pop
                d. Exit Column""")

        #verifying the column selection
        while True:
            col_choice = str(input("Please enter the column: ")).casefold()
            if (col_choice not in ('a', 'b', 'c', 'd')):
                print("\nNot an appropriate choice.\n")
            else:
                break
            
        #if column (a) is seleced
        if (col_choice == "a"):
            #Then prints the column name
            print("You selected Pop Apr 1")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = pop_df["Pop Apr 1"].describe()
            print(desc)
            #ploting the graph
            plt.hist(pop_df["Pop Apr 1"],bins = 100)
            #Assign to a figure
            fig_a=plt
            # Save Figure for Download
            fig_a.savefig('Pop Apr 1.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu
            
        #if column (b) is seleced
        elif (col_choice == "b"):
            #Then prints the column name
            print("You selected Pop Jul 1")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = pop_df["Pop Jul 1"].describe()
            print(desc)
            #ploting the graph
            plt.hist(pop_df["Pop Jul 1"],bins = 100)
            #Assign to a figure
            fig_b=plt
            # Save Figure for Download
            fig_b.savefig('Pop Jul 1.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu
            
        #if column (c) is seleced
        elif (col_choice == "c"):
            #Then prints the column name
            print("You selected Change Pop")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = pop_df["Change Pop"].describe()
            print(desc)
            #ploting the graph
            plt.hist(pop_df["Change Pop"],bins = 100)
            #Assign to a figure
            fig_c=plt
            # Save Figure for Download
            fig_c.savefig('Change Pop.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu
            
        else:
            #exiting the column menu and going back to main menu
            print("\nYou selected to exit the column menu\n")
            main() #recurrsive call of the main menu



    #performing the operation for the selection 1
    elif (selection == 2):
        hs_df = pd.read_csv("Housing.csv")
        print("""Select the Column you want to analyze:
                a. AGE
                b. BEDRMS
                c. BUILT
                d. ROOMS
                e. UTILITY
                f. Exit Column""")
        
        while True:
            col_choice = str(input("Please enter the column: ")).casefold()
            if (col_choice not in ('a', 'b', 'c', 'd','e','f')):
                print("\nNot an appropriate choice.\n")
            else:
                break
            
        #if column (a) is seleced
        if (col_choice == "a"):
            #Then prints the column name
            print("You selected AGE")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = hs_df["AGE"].describe()
            print(desc)
            #ploting the graph
            plt.hist(hs_df["AGE"],bins = 100)
            #Assign to a figure
            fig_a=plt
            # Save Figure for Download
            fig_a.savefig('AGE.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu
            
        #if column (b) is seleced
        elif (col_choice == "b"):
            #Then prints the column name
            print("You selected BEDRMS")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = hs_df["BEDRMS"].describe()
            print(desc)
            #ploting the graph
            plt.hist(hs_df["BEDRMS"],bins = 100)
            #Assign to a figure
            fig_b=plt
            # Save Figure for Download
            fig_b.savefig('BEDRMS.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu
            
        #if column (c) is seleced
        elif (col_choice == "c"):
            #Then prints the column name
            print("You selected BUILT")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = hs_df["BUILT"].describe()
            print(desc)
            #ploting the graph
            plt.hist(hs_df["BUILT"],bins = 100)
            #Assign to a figure
            fig_c=plt
            # Save Figure for Download
            fig_c.savefig('BUILT.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu

        #if column (d) is seleced
        elif (col_choice == "d"):
            #Then prints the column name
            print("You selected ROOMS")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = hs_df["ROOMS"].describe()
            print(desc)
            #ploting the graph
            plt.hist(hs_df["ROOMS"],bins = 100)
            #Assign to a figure
            fig_c=plt
            # Save Figure for Download
            fig_c.savefig('ROOMS.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu

        #if column (e) is seleced
        elif (col_choice == "e"):
            #Then prints the column name
            print("You selected UTILITY")
            
            print("The statistics for this column are:")
            #using the describe method to get all the stats
            desc = hs_df["UTILITY"].describe()
            print(desc)
            #ploting the graph
            plt.hist(hs_df["UTILITY"],bins = 100)
            #Assign to a figure
            fig_c=plt
            # Save Figure for Download
            fig_c.savefig('UTILITY.svg')
            print("\nThe Histogram of this column can be downloaded now.")
            #showing the graph
            plt.show()
            main() #recurrsive call of the main menu

        else:
            #exiting the column menu and going back to main menu
            print("\nYou selected to exit the column menu\n")
            main() #recurrsive call of the main menu



#main method to call the all the functions
def main():
    while True:
        ch = menu()
        operations(ch)


#calling all the functions
if __name__ == "__main__":
    main()

#importing the module numpy as np for ease
import numpy as np

##GLOBALLY DECLARATION OF THE NUMPY ARRAY
global matrix_1
global matrix_2

#declaring the empty matrix
matrix_1 = np.zeros([3,3])
matrix_2 = np.zeros([3,3])


#creating the menu
def menu():
    #try and catch block to handle exception errors
    try:
        print("""\nEnter choice:
                1.Matrix Addition
                2.Matrix Subtraction
                3.Matrix Multiplication
                4.multiplication element by element
                5.exit""")
        #prompting user for the input
        global choice
        choice = int(input())
        #in case if the choice is greater than menu options
        while ( choice > 6):
            choice = int(input("Please re-enter your choice correctly"))
    #handling the value error
    except ValueError:
        print("Enter appropriate choice as number")
        menu()    #function call itself again for choice

    #retrieving the choice
    return choice


def create():
    
    def enter():# if user enter value rather than integer and float then this function call to enter appropriate value for first array
        try:
            matrix_1[i][j] = input()
        except ValueError:
            print("Enter integer or float only")
            enter()    # recursion will occur until user enter integer or floating point value

    print("enter elements of first array")
    for i in range(3): #entering element by index in first matrix
        for j in range(3):
            try:
                print("Enter the element for "+str(i+1)+" row and "+str(j+1)+" column.")
                matrix_1[i][j] = input()
            except ValueError:
                print("Enter integer or float only")
                enter()
    print("Your first matrix\n",matrix_1)


    def enter(): # if user enter value rather than integer and float then this function call to enter appropriate value for second  array
        try:
            matrix_2[i][j] = input()
        except ValueError:
            print("Enter integer or float only")
            enter()  # recursion will occur until user enter integer or floating point value

    print("enter elements of Second array")
    for i in range(3):   #entering element by index in second matrix
        for j in range(3):
            try:
                print("Enter the element for "+str(i+1)+" row and "+str(j+1)+" column.")
                matrix_2[i][j] = input()
            except ValueError:
                print("Enter integer or float only")
                enter()
    print("your second matrix\n",matrix_2)

'''
    .mean() => calculates the mean
    .add() => add the elements
    .subtract => find the difference between the elements
    .T => find the transpose
    axis = 0 is for row
    axis = 1 is for column
'''
#function to perform operations
def selection():
    if (choice == 1):
        result = np.add(matrix_1,matrix_2)  #matrix addition
        print("Resultant matix\n") 
        print(result)
        print("Transpose of resultant matrix")
        print(result.T)
        print("Mean of coloumn")
        print(np.mean(result, axis=1))
        print("Mean of rows")
        print(np.mean(result, axis=0))
        menu() # show available option
        selection()
    elif(choice==2):
        result = np.subtract(matrix_1,matrix_2)  #matrix subtraction
        print("Resultant matix\n")
        print(result)
        print("Transpose of resultant matrix")
        print(result.T)
        print("Mean of coloumn")
        print(np.mean(result, axis=1))
        print("Mean of rows")
        print(np.mean(result, axis=0))
        menu() # show available option
        selection()
    elif(choice==3):
        result=np.matmul(matrix_1, matrix_2)  #matrix multiplication
        print("Resultant matix\n")
        print(result)
        print("Transpose of resultant matrix")
        print(result.T)
        print("Mean of coloumn")
        print(np.mean(result, axis=1))
        print("Mean of rows")
        print(np.mean(result, axis=0))
        menu() # show available option
        selection()
    elif(choice==4):
        result = np.multiply(matrix_1,matrix_2)#element by element multiplication
        print("Resultant matix\n")
        print(result)
        print("Transpose of resultant matrix")
        print(result.T)
        print("Mean of coloumn")
        print(np.mean(result, axis=1))
        print("Mean of rows")
        print(np.mean(result, axis=0))
        menu()  # show available options
        selection()
    elif(choice==5):
        exit  #to quit


create()
menu()
selection()



            

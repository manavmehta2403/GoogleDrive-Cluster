import numpy as np
global a   #declare globally for use in whole program and its function
global b
a = np.zeros([3, 3])  #creation of 3x3  array for matrices
b = np.zeros([3, 3])

def create():   #create two numpy array

    def enter():      # if user enter value rather than integer and float then this function call to enter appropriate value for first array
        try:
            a[i][j] = input()
        except ValueError:
            print("Enter integer or float only")
            enter()    # recursion will occur until user enter integer or floating point value

    print("enter elements of first array")
    for i in range(3): #entering element by index in first matrix
        for j in range(3):
            try:
                a[i][j] = input()
            except ValueError:
                print("Enter integer or float only")
                enter()
    print("Your first matrix\n",a)


    def enter(): # if user enter value rather than integer and float then this function call to enter appropriate value for second  array
        try:
            b[i][j] = input()
        except ValueError:
            print("Enter integer or float only")
            enter()  # recursion will occur until user enter integer or floating point value

    print("enter elements of Second array")
    for i in range(3):   #entering element by index in second matrix
        for j in range(3):
            try:
                b[i][j] = input()
            except ValueError:
                print("Enter integer or float only")
                enter()
    print("your second matrix\n",b)
    appropriate()


global choice   #globally declared to use in whole program
def selection():
    if (choice == 1):
        c = a + b  #matrix addition
        print("resultant matix\n")
        print(c)
        print("transpose of resultant matrix")
        print(c.T)
        print("mean of coloumn")
        print(np.mean(c, axis=0))
        print("mean of rows")
        print(np.mean(c, axis=1))
        appropriate() # show available option
    elif(choice==2):
        c = a - b   #matrix subtraction
        print("resultant matix\n")
        print(c)
        print("transpose of resultant matrix")
        print(c.T)
        print("mean of coloumn")
        print(np.mean(c, axis=0))
        print("mean of rows")
        print(np.mean(c, axis=1))
        appropriate() # show available option
    elif(choice==3):
        c=np.matmul(a, b)  #matrix multiplication
        print("resultant matix\n")
        print(c)
        print("transpose of resultant matrix")
        print(c.T)
        print("mean of coloumn")
        print(np.mean(c, axis=0))
        print("mean of rows")
        print(np.mean(c, axis=1))
        appropriate() # show available option
    elif(choice==4):
        c = a*b #element by element multiplication
        print("resultant matix\n")
        print(c)
        print("transpose of resultant matrix")
        print(c.T)
        print("mean of coloumn")
        print(np.mean(c, axis=0))
        print("mean of rows")
        print(np.mean(c, axis=1))
        appropriate()  # show available option
    elif(choice==5):
        create() #re create two matrices
    elif(choice==6):
        pass  #no function call it is end of program



def appropriate():    #user must enter integer value for given choice
    try:
        print("\n enter choice:\n1.Matrix Addition\n2.Matrix Subtraction\n3.Matrix Multiplication \n4.multiplication element by element\n5.Re-enter all two matrices\n6.exit")
        global  choice
        choice=int(input())
        selection()
    except ValueError:
        print("enter appropriate choice")
        appropriate()    #function recursion until user enters appropriate value


create()    #program  exceution starting by creation of matrices by calling the function

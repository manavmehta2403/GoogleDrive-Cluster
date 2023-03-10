####indentation ( gaps ) is used to tell that the part belongs some statements
##
##a = 5
##
##if (a==5): ##True 
##    print("Value of a is",5)
##    b=6
##    print(b)
##
##else:
##    print("Value of a is not",5)
##
##
##
##
##
####Selectional statements ya conditions statements ya if n' else,
####they check the conditions and return true ya false (boolean)
####if any condition statement is true then that condition code block will run
##
####elif is used to check more than one condition
##
#####lets take two numbers from user and find largest from them.
##
##print("Manav algo")
###prompt user to enter the numbers
##num1 = float(input("Please enter the first number: ")) ##43
##num2 = float(input("Please enter the second number: ")) ##34
##
###checking whether the first number is greater
##if ( num1 > num2 ): 
##    print ("Number 1 is greater")
##    
### checking whether the second number is greater
##elif ( num1 < num2 ):
##    print ("Number 2 is greater")
##
### otherwise they both will be equal
##else:
##    print("Both numbers are equal")
##
##print() ## for addind line space
##
##
##print("Puru algo")
###prompt user to enter the numbers
##number1 = float(input("Please enter the first number: ")) ##43
##number2 = float(input("Please enter the second number: ")) ##34
##
### checking whether the numbers are equal
##if ( number1 == number2 ):
##    print("Both numbers are equal")
##    
### checking whether the second number is greater
##elif ( number1 < number2 ):
##    print ("Number 2 is greater")
##
### otherwise the first number is greater
##else:
##    print ("Number 1 is greater")
##
##
##
###Some questions
##x = 45 ### x 45
##
##if (x > 45): ##false
##    print("Puru")
##else:
##    print("Manav")
##
##print("Nikhil")
##
##########################################################
##
##x = 56
##
##if ( x > 45):
##    print("Puru")
##    
##else:
##    print("Nikhil")
##    print("Manav")
##
##print("Meenu")
##
##
#######################################################
##
##x = "Big Brother"
##
##if (x == "big brother"):
##    print("Correct")
##
##elif (x == "BigBrother"):
##    print("Incorrect")
##
##elif (x == "Big Brother"):
##    print("tricky")##tricky
##
##else:
##    print("Not so smart")
##
##x = x * 2
##
##print(x)##(1) Big Brother Big Brother or ##(2) Big BrotherBig Brother or ##(3) BigBrotherBigBrother
##
#########################################################
##
##
##
####Nested if and else (with elif): if else ke andr he if else


numb1 = int(input("Please enter the first number: "))
numb2 = int(input("Please enter the second number: "))
numb3 = int(input("Please enter the third number: "))


if ( numb1 >= numb2 and numb1 >= numb3):
            print(numb1, "is largest")
    
elif ( numb2 >= numb1 and numb2 >= numb3):
            print(numb2, "is largest")

elif ( numb3 >= numb1 and numb3 >= numb2):
            print(numb3, "is largest")

else:
    print("All three are equal")


print("Printing answer using nested if else")

if (numb1 >= numb2):
    if (numb1 >= numb3):
        print(numb1, "is largest")
    else:
        print(numb3, "is largest")
        
elif (numb2 >= numb1):
    if (numb2 >= numb3):
        print(numb2, "is largest")
    else:
        print(numb3, "is largest")





##Puru leap years
year = int(input("Pleae input the year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  print("It is a leap year.")
else:
  print("It is not a leap year.")

###nested if else
if (year % 4 == 0):
  if (year % 100 != 0):
    print("It is a leap year.")
  elif (year % 400 == 0):
    print("It is a leap year.")
  else:
    print("It is not a leap year.")


















    

    
    


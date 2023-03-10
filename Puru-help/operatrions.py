## operators and operands


##Operands are those on which operators perform operations. #Ex: Data-types

##Operators are the special symbols or keywords to perform operations.



##1. Assign operator (universal operator) (=)
    ##It is used to assign values to the variables
abc = 34.6
xyz = "yo-yo"

##These equal to signs are known as assign operators

###They are some operators which also work on structured datatypes like (+) & (*) & (**)###

##2. Arithmetic operators

    ##Addition (+) it work on string, & numbers (int, float)

        ##if + is performed on string it will concate (join) the string

first_name = str(input("Please enter your first name: "))
last_name = str(input("Please enter your last name: "))

print(first_name+last_name)

##we can concate gap(space) in between them

print(first_name+" "+last_name)


            ## if + is performed on numbers it will add them
num1 = 6
num2 = 7
print(num1+num2)


            ##if i use + operator with string as well as with number
##string = "Purva"
##number = 6
##print(string+number) ###it will give error because it will get confuse
## either add or concate

###addition operator
number1 = 7
number2 = 10.0

print(number1 + number2)

##17  ==> int
##17.0 ==> float

###float is considered more presendence (prior) than int


        ##Subtraction (-) it work on numbers (int, float)
            ##it used to minus the numbers

no1 = 56
no2 = 50

print(no1 - no2)


        ##Asterik (*) it works on string, & numbers (int, float)

        ##in string asterik produces the same string number of times.
string = "Puru is awesome"
print(string+string+string+string+string+string)

print(string*6) ##//Puru is awesomePuru is awesomePuru is awesome...

        ##numbers multiply two operands

n1 = 24
n2 = 6
print(n1 * n2)

        ##Double Asterik (**) it used as exponent works on numbers (int, float)
nu1 = 45
nu2 = 2
print(nu1 ** nu2)

        ## Slash (/) it is used to divide in float and give quotient
numb1 = 21
numb2 = 5
print(numb1 / numb2)

        ## Double Slash (//) it is used to divide in int and give quotient. Floor division
numb1 = 21
numb2 = 5
print(numb1 // numb2)

        ##Modulus (%) it is used to give remainder
n_1 = 21
n_2 = 5
print(numb1 % numb2)


#The acronym PEMDAS is a useful way to remember the rules:
#Parentheses(), Expoent**, Multiplication *, Division /,//,% , Addition + and Subtraction -

## Add and Assign(+=)
##Adds the values on either side and assigns it to the expression on the left.
##a+=10 is the same as a=a+10.
##The same goes for all the next assignment operators.
##a+=2 print(a) Output: 9
a = 4
a = a + 2
print("Result1",a)
a = 4
a += 2 ### a = a+2
print("Result2",a)
## Subtract and Assign(-=)
##Subtracts the value on the right from the value on the left.
##Then it assigns it to the expression on the left.
##a-=2 print(a) Output: 7
a = 4
a = a - 2
print("Result1",a)
a = 4
a -= 2 ### a = a-2
print("Result2",a)
##Divide and Assign(/=)or(//=)
##Divides the value on the left by the one on the right.
##Then it assigns it to the expression on the left.
##a/=7 print(a) Output: 1.0
a = 4
a = a / 2
print("Result1",a)
a = 4
a /= 2 ### a = a/2
print("Result2",a)
##Multiply and Assign(*=)
##Multiplies the values on either sides.
##Then it assigns it to the expression on the left.
##a*=8 print(a) Output: 8.0
##
##Modulus and Assign(%=)
##Performs modulus on the values on either side.
##Then it assigns it to the expression on the left.
##a%=3 print(a) Output: 2.0
a = 5
a = a % 2
print("Result1",a)
a = 5
a %= 2 ### a = a%2
print("Result2",a)
##Exponent and Assign(**=)
##Performs exponentiation on the values on either side.
##Then assigns it to the expression on the left.
##a**=5 print(a) Output: 32.0
a = 4
a = a ** 2
print("Result1",a)
a = 4
a **= 2 ### a = a**2
print("Result2",a)
##Floor-Divide and Assign(//=)
##Performs floor-division on the values on either side.
##Then assigns it to the expression on the left.
##a//=3 print(a) Output: 10.0
a = 4
a = a // 2
print("Result1",a)
a = 4
a //= 2 ### a = a//2
print("Result2",a)


##########################################################################################
#    ##ASCII Values for capital alphabhets is 65 - 90                                    #
#    ##ASCII values for smaller alphabhets is 97 - 122                                   #
#
print("A" > "Z") ##65 > 90 = False                                                      
print("a" > "A") ##97 > 65 = True
#                                                                                        #
#                                                                                        #
#    ## To find ASCII value of any character (sinlge string) - ord()                     #
print(ord("a"))
print(ord("@"))
#                                                                                        #
#   ##To find charter from ascii values - chr()
print(chr(97))
print(chr(113))
#                                                                                        #
##########################################################################################


##3. Relational Operators
##these operators are used to tell whether the given statement is True or False,
##they return boolean value.

    ##less than (>) it is used to check whether the given value is smaller
print("Puru">"Purv") ##(P)80=80,(u)117=117,(r)114=114,(u)117 < 118(v)
print("Puru">"Muru") ##(P)80 > 77(M)

print(89 > 90)

print(90 > 90)


  ##more than (<) it is used to check whether the given value is larger
print("Nikhil" < "Puru") ## (N)78 < 80(P)


  ##double (==) is used to check whether the given values are equal

print(90 == 90)


    ## not equal to (!=) is used to check whether given values are not equal
print(80 != 90)

    ## we can use two operator together (>=) or(<=)

print(80 >= 90)
print(90 >= 90)
print(100 >= 90)

##3. Logical Operators
###They also return boolean values like True and False.

    ##and
        ##if all the statements is true then it is true
boolean = 5 > 7 and 6 > 4
print(boolean)
boolean = 5 < 7 and 6 > 4
print(boolean)

    ##or
        ##if any one statement is true then it is true
boolean = 5 > 7 or 6 > 4
print(boolean)
boolean = 5 < 7 or 6 > 4
print(boolean)
boolean = 5 > 7 or 6 < 4
print(boolean)

    ##not
        ##if it is true then I will make false or if its false, then I will make it true
boolean = not ( 7 > 4)
print(boolean)
boolean = not(5 < 7 or 6 > 4)
print(boolean)
boolean = 5 > 7 or 6 < 4 ##false
print(not(boolean)) ##true

##Special operators
        ###is operator - it is used to check whether data is null or not
        ### is can be used as == but python will generate warning
null = None
print(null is None)

number = 65
print (number is 65)

##Always remember not is wrong way of writing always write is not
null = None
print(null is not None)
        ###in operator - it used to check whether literals comes inside the data or not

name = "Puru Mehta"
print( "p" not in name)


##Binary operators works on 0 and 1 as bits of the computer.


##Binary AND(&)

##It performs bit by bit AND operation on the two values.
##Here, binary for 2 is 10, and that for 3 is 11. &-ing them results in 10,
##which is binary for 2. Similarly, &-ing 011(3) and 100(4) results in 000(0).

##AND (&) = 0 and(x) 1
##0 & 0 = 0
##0 & 1 = 0
##1 & 0 = 0
##1 & 1 = 1

print(2&3)


##2&3 Output: 2

##3&4 Output: 0

##b. Binary OR(|)

##It performs bit by bit OR on the two values. Here, OR-ing 10(2) and 11(3) results in 11(3).
##
##2|3 Output: 3
##OR (|) = 0 or(+) 1
##0 | 0 = 0
##0 | 1 = 1
##1 | 0 = 1
##1 | 1 = 1

print(2|3)


###Questions
print(4&6)

print(3|9)

##i Binary One’s Complement(~)
##
##It returns the one’s complement of a number’s binary.
##It flips the bits. Binary for 2 is 00000010. Its one’s complement is 11111101.
##is binary for -3. So, this results in -3. Similarly, ~1 results in -2.
##
##~-3 Output: 2
##
##Again, one’s complement of -3 is 2.
##
print(~2)


##ii. Binary Left-Shift(<<)
##
##It shifts the value of the left operand the number of places to the
##left that the right operand specifies. Here, binary of 2 is 10.
##2<<2 shifts it two places to the left. This results in 1000, which is binary for 8.
##
##2<<2 Output: 8
##
print(2<<2)
##iii. Binary Right-Shift(>>)
##
##It shifts the value of the left operand the number of
##places to the right that the right operand specifies.
##Here, binary of 3 is 11. 3>>2 shifts it two places to the right.
##This results in 00, which is binary for 0.
##Similarly, 3>>1 shifts it one place to the right. This results in 01, which is binary for 1.
##
##3>>2 3>>1 Output: 1

print(2>>2) 


###Convert binary number into decimal
print(int('100',2)) ###binary numbers are always written in single quotes
###Convert decimal into binary
print(bin(2))  ## 0b10 ==> number before b tells the sign and after b is the value






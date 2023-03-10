##Data -types are the different types of data that python can store
##() = parenthesis
##Data-types
##1. Primitive datatypes which are used to store single data
##2. Structure datatypes which are used to store mutliple data
##
##Primitive datatypes
##1. String - str() - It is used to store aplhanumeric (alphabhets,numbers,@#)
##            #and sepcial characters.(@$&)
##            #They always start and end with either single ('')quote or
##            #double quote (" ").
##            #Programmer prefer string with double quotes (" ")
##
##        ### we can use triple single quotes or triple double quotes to print same format
##
string1= "Ram's dad is awesome."
print(string1)

string = 'Puru always rock the world.'
print(string)

###Write your first name and last name and then print it
name="purva mehta"
print(name)

##Write a string where you write our name and print it.
name="purva"
print(name)

#Let take user surname
surname = str(input("Please enter your last name: "))
print(surname)

#Ask student father name
father_name = str(input("Enter your father's name: "))
print(father_name)




print("Hello")
print ("mister how are")
print("you")


print("""Hello
mister  how are
you""")



print("""Mᴇʟᴀɴɪᴇ Mᴀʀᴛɪᴇɴᴇᴢ- Dᴇᴛᴇɴᴛɪᴏɴ
0:35 ━━━❍───── -5:32
↻     ⊲  Ⅱ  ⊳     ↺
VOLUME: ▁▂▃▅▆▇ 100%""")



#2. Integer - int() - it used to store numbers without decimals (integers).

num = 65
print(65)

num2 = "653" ### as it is in double quotes/single quote then it is a string
print(num2)


integer_number = int(input("Enter the number: "))
print(integer_number)

##3. Decimal - float() - it used to to store numbers with decimals.

num1 = 4523.8
print(num1)

decimal_number = float(input("Enter the decimal number: "))
print(decimal_number)

##4. Complex - (+j) imaginary numbers that exits in maths

img = 45+63j
print(img) ### it used in scientific calculations

##5. Boolean - bool() - python can store true and false (True or False)


check = 8 > 9
print(check)

boolean = bool(input("Enter either True or False: "))
## boolean store True aap jo marzi true he store kre ga
print(boolean)

##6. NoneType - None - it used to tell null value (empty ja pr kuch na ho)
null = None
print(null)








##type () is a function which used to tell the data-type of the variable
print(type(num)) ## int
print(type(num2)) ## str
print(type(num1)) ## float
print(type(img)) ##complex
print(type(check)) ##bool
print(type(null)) ##none





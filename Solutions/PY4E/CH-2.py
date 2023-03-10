# **Chapter 2**

#Q1 
5 ## random with no variable will be consider simple int
x = 5 ## 5 is assign to x
x + 1 ## one will be added to x


#Q2
name = str(input("Please enter your name: "))
print("Hello",name)

#Q3
try: 
  ##prompt user for the hours value
  hours = float(input("Please enter hours: "))
  ##prompt user for the rate value
  rate = float(input("Please enter rate: "))
  ##calculate payment using the formula hours * rate
  pay = hours * rate
  ##dsiplaying the output
  print("Pay:",pay)


  ##now python has in-built function called round (will be studing in the 
  ## coming chapters to round off the figure)
  ####round is the in built function for the float data type 
  ###that take two parameters first as float and second as
  ### the decimal place to round off as int
  pay = round(hours * rate,2)
  print("Pay:",pay)
except:
  print("Some values are enter were wrong!!!.")

#Q4
width = 17
height = 12.0

###
print(width//2) #to get the floor division (quotient as int) of width that is 8
print(width/2.0) # to get the quotient that is 8.5
print(height/3) # it also give quotient as float 4.0
print(1 + 2 * 5) ## will print 11 PEMDAS

#Q5
try:
  #prompting user for the temperature in celsius
  cel = float(input("Please enter the temperature in celsius: "))
  #converting temperature in fahrenheit
  far = (cel * 9/5) + 32
  #display fahrenheit temperature
  print("Temperature in fahenheit is",far)

  #converting temperature in kelvin
  kel = cel + 273.15
  #displaying temperature in kelvin
  print("Temperature in kelvin is",kel)
except:
  print("Values might have been entered is wrong!!!!.")

##There two types of errors

###Bug means error and debugs removing errors


##Syntax means grammar of programming language

##Syntax error: Those errors which occur due to wrong way of writing code
##that python cannot understand.


#primt("Puru") ###primt is wrong keyword for output, we must used print

print("Puru")


##Syntax can be removed very easily using eval('')

eval('primt("Puru")')

##Logical error: Those errors in which program execute propery but output is wrong
## These  are hard to debug.

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
##lets add these two numbers
print(num1 - num2) ## there we have made a logical error we used - instead +

print(num1 + num2)

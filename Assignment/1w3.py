#declaring and initializing the variable
stop = 'go'
#looping over the stop to check stop should not equal to q
while (stop!='q'):
    #prompting user to ask the nuber of the inputs
    #NOTE str is for string, for integer use int and for decimal use float
    quantity = str(input('Quantity purchased:\n'))
    #prompt user to ask whether they want to continue or not
    #casefold() is to make the input case-insensetive.
    stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n").casefold()

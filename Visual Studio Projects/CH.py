import random #module to generate random numbers
def lotgenerator(choice): #method to generate numbers
    lottery_numbers = [] #list for entering the numbers one by one in the list
    if (choice == 3 or choice == 4): #checking the choice either 3 or 4
        while(choice != 0): #sequential while loop till choice is not equal to zero
            rand = random.randint(0,9) #generating the random numbers and storing in the rand
            if (rand >= 0 and rand <= 9): #checking the number is between 0 and 9
                lottery_numbers.append(rand) #entering the number in the list
            choice -= 1 #decrement in choice variable to loop out from the loop
    '''use return lottery_numbers in case if you are not fimiliar with join and map'''
    return ''.join(map(str, lottery_numbers)) #casting the list as the string using join with map


ch = int(input("Enter generator choice: ")) #prompting the user for the choice
while  not ch in (3, 4): #loop to check the validation of the user input
    ch = int(input("Wrong choice. Please enter 3 or 4: ")) #asking the input again if it is invalid
print("The lottery number is: ", lotgenerator(ch)) #calling the lottery generator

print("-------------------------------XXXXXXXXXXXXXXXXXX-------------------------------")

#calling all the essential libraries
import math #math module for the math terms
import numpy #for arange to loop over the float values

#method to find the sin and cos values between -2pi and 2pi
def trigonometryfunction():
    sinx=[] #list for the sin(f(x)) values
    cosx=[] #list for the cos(f(x)) values
    Xvalues=[] #list for the x values of trignometry
    for x in numpy.arange(-2*math.pi,2*math.pi+(math.pi/64),math.pi/64): #iterating over the -2pi and 2pi increasing by pi/64
        Xvalues.append(x) #values of x
        sinx.append(math.sin(x)) #adding sin(f(x)) values using math.sin for sin values
        cosx.append(math.cos(x)) #adding cos(f(x)) values using math.cos for cos values
    return Xvalues, sinx, cosx #returning the values of x, sinx and cosx list


def algebraicfunction():
    sqrtx=[] #list to hold the sqrt(f(x)) values
    log10x=[0] #list to hold the log10(f(x)) values ##ZERO is inserted before hand as log10(0) is not defined in maths
    Xvalues=[] #list for the x values for algebraic
    for x in numpy.arange(0,200+(0.5),0.5): #iterating over the 0 and 200 increasing by 0.5
        Xvalues.append(x) #values of x 
        if(x == 0): #loop to continue if x is zero as log10(0) is not defined in maths
            sqrtx.append(math.sqrt(x)) #adding sqrt(f(0)) value because sqrt(0) is 0 in maths
            continue
        sqrtx.append(math.sqrt(x)) #adding sqrt(f(x)) values
        log10x.append(math.log10(x)) #adding log10(f(x)) values
    return Xvalues, sqrtx, log10x #returning the values of x, sqrtx and log10x list



#displaying the values for the trigonometry function and storing respective list in the variables
trigox,siny,cosy = trigonometryfunction()
print("Values of x for trigonometric functions: ", trigox)
print("\n")
print("Values of sin(f(x)): ", siny)
print("\n")
print("Values of cos(f(x)): ", cosy)
print("\n")


#displaying the values for the algebaric function and storing in the variables
algx,sqrty,logy = algebraicfunction()
print("Values of x for algebraic  functions: ", algx)
print("\n")
print("Values of sqrt(f(x)): ", sqrty)
print("\n")
print("Values of log10(f(x)): ", logy)


'''To update  the values in the csv files'''
import pandas as pd

columns_trigo = {}

columns_trigo['value_of_trigo_x'] = trigox
columns_trigo['sin(f(x))'] = siny
columns_trigo['cos(f(x))'] = cosy

trigo_func = list(zip(columns_trigo['value_of_trigo_x'],columns_trigo['sin(f(x))'],columns_trigo['cos(f(x))']))

df_trigo = pd.DataFrame(data = trigo_func)

df_trigo.to_csv('trigo.csv', index=False, header=['value_of_trigo_x','sin(f(x))','cos(f(x))'])


columns_alg = {}

columns_alg['value_of_alg_x'] = algx
columns_alg['sqrt(f(x))'] = sqrty
columns_alg['log10(f(x))'] = logy

alg_func = list(zip(columns_alg['value_of_alg_x'],columns_alg['sqrt(f(x))'],columns_alg['log10(f(x))']))

df_algo = pd.DataFrame(data = alg_func)

df_algo.to_csv('algo.csv', index=False, header=['value_of_alg_x','sqrt(f(x))','log10(f(x))'])




"""IF YOU WANT USE YOUR OWN GRAPHING TOOL YOU CAN DELETE THIS BELOW THIS LINE"""
'''NOTE THIS IS GRAPHING TOOL OF PYTHON'''
import matplotlib.pyplot as plt #to plot the graphs
def graph():
    #making the subplots (row, columns, figure) one row with two columns and this is the first plot
    plt.subplot(2,1,1)
    #plotting x and sin(f(x)) and cos(f(x)) where b is blue and -- dashed line and c is cyan and : dotted line
    plt.plot(trigox, siny,"y-", trigox, cosy,"g-.")
    #labelling the x, y, tiltle and legend
    plt.xlabel('x values from -2pi to 2pi')
    plt.ylabel('sin(x) and cos(x)')
    plt.title('Plot of sin and cos from -2pi to 2pi')
    plt.legend(['sin', 'cos'])
    plt.subplots_adjust(hspace = 0.6, wspace = 0.6)
    #now figure 2 means graph 2
    plt.subplot(2,1,2)
    #plotting x and sqrt(f(x)) and log10(f(x)) where y is yellow and - solid line and g is green and -. dashed dotted line
    plt.plot(algx,sqrty,"r--",algx,logy,"b:")
    #labelling the x, y, tiltle and legend
    plt.xlabel('x values from 0 to 200')
    plt.ylabel('sqrt(x) and log10(x)')
    plt.title('Plot of sqrt and log from 0 to 200')
    plt.legend(['sqrt', 'log10'])

    #dsiplay the graph
    plt.show()

#calling the function
graph()



##18993215
def main():
    #taking two list one for time and another for concenteration
    time=[]
    concentration = []
    #intializing the concentration and time variable as one
    c = 0.00
    t = 0.00

    #as for loop cannot iterate over the float numbers
    #while loop will help to iterate the time variable till 2
    while t <= 2:
        #inserting time variable in the list
        time.append(t)
        #calculating the variable c value using formula
        c = (12*(t**2) - 15*t + 12)/((t**2)+1)
        #adding the concenteration variable to list
        concentration.append(c)
        #calculating time variable b stepping 0.01 every-time,
        #to remove floating-point logical error
        #round off is done at every step to decimal place 2
        t = round((t + 0.01),2)

    #printing time list
    #print(time)
    #print()

    #printing concenteration list
    #print(concentration)
    #print()

    #iterating over the range of 0 to length pf time
    for i in range (0,len(time)):
        #if the index of any concenteration is equal to minimum concenteration
        if(min(concentration) == concentration[i]):
            #concenteration of that index is print with the time at that index
            print("The minimum concentration is " + str(concentration[i]) + " at time " + str(time[i]) + "min")

    """####verifying the result
    print(time.index(1.0),concentration.index(min(concentration)))"""

if __name__ == "__main__":
    main()

def main():
    #taking two list one for time and another for concenteration
    concentration = []
    time=[]
    #intializing the concentration and time variable as 0
    c = 0.00
    t = 0.00
    #running the loop till it meets the breaking condition
    while True:
        #inserting time variable in the list
        time.append(t)
        #calculating the variable c value using formula
        c = (12*(t**2) - 15*t + 12)/((t**2)+1)
        #adding the concenteration variable to list
        concentration.append(c)
        t =((t + 0.01),2)
        if (abs(c - 12) < (10**-3)):
            break

    ##now removing the first element as 12 and its time
    for i in range (0,len(concentration)):
        if (concentration[i] == 12):
            concentration.remove(12)
            time.pop(i)
            break

    ##dragging the time variable when concenteration is 12
    for i in range (0,len(concentration)):
        if (concentration[i] == 12):
            print("At " +str(time[i]/60)+"hours concentration will be 12 again.")
    else:
        print("This concentration do not repeat itself")

if __name__ == "__main__":
    main()

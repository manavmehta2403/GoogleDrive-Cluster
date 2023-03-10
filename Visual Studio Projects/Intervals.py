def main():
    #list to store the tuple values
    intervals = []
    #open file to read 
    with open("intervals.txt", "r") as file:
        #reading every line in the file
        for line in file:
            #getting values by separated by the space
            values = line.split(" ")
            #adding values in the list as tuples
            intervals.append((int(values[0]), int(values[1])))

    #sorting the list
    intervals = sorted(intervals)

    #print(intervals) #testing how sort is performed

    #empty list to get only the non-interecting tuples
    merged = []

    #looping over the intervals to check the higher value
    for high in intervals:
        #if the higher variable is not in the list that is adding the first element followed by the others
        if not merged:
            merged.append(high)
        #check the other values
        else:
            #taking the last element of the list then followed by the other elements
            low = merged[-1]
            #intersection between lower and higher
            #through sorting that low[0] <= high[0]
            if high[0] <= low[1]:
                #find the max upper bound
                upper = max(low[1], high[1])
                merged[-1] = (low[0], upper)  # replace by merged interval
            else:
                #adding thoses values that is lower than higher variable
                merged.append(high)

    #printing the result
    for i in range (0,len(merged)):
        print (merged[i])

if __name__ == "__main__":
    main()


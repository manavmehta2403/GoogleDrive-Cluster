#creating 2D list of the parity 
def linear_block_code():
    #2D list
    parity  = [["Y","Y","Y","Y","N","N"],["Y","Y","N","N","Y","Y"]]
    #printing the list
    #iterating over the row
    for i in range(len(parity)):
        #print the parity number as per the row number
        if ( i == 0 ):
            print("Parity 1: ", end ="")
        if ( i == 1):
            print("Parity 2: ", end ="")
        #iterating over the column
        for j in range(len(parity[i])):
                print(parity[i][j],end = ' ')
        print()
    #return the list
    return parity

#probablity calculator
def prob_cal(parity):
    #finding the number of Y in the list
    count = sum(elem.count('Y') for elem in parity)
    print("No of the bits not flipped:",count)
    
    #none flip prob given
    prob_notflip = 0.1

    #prob of event A
    pA = (1 - prob_notflip)**count
    print("(a). Probability when none of the bits are flipped:",pA)

    #prob of flip
    prob_someflip = 1 - pA

    #"""There is fifty-fifty chance of getting detected by the parity check"""
        
    #prob of event B
    pB = prob_someflip/2
    print("(b). Probability when flipped and detected:",pB)
    #prob of event C
    pC = (1 - pA) * (1/2)
    print("(c). Probability when flipped and not detected:",pC)
    
#main method
def main():
    #calling the parity  2D list
    par = linear_block_code()
    print()
    #passing the par as parameter for calculating the parameter
    prob_cal(par)
    print()

    
    
    ##checking the test case
    print("If the original data is 111111, then, the parity bits will be 00.")
    pari  = [[1,1,1,1,1,1],[1,1,1,1,1,1]]
    prob_cal(pari)

#running the main method
if __name__ == "__main__":
    main()

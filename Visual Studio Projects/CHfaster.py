def main():
    # try and except block will run the loop till any value error exception
    try:
        #empty set of weight
        weights = [] 
        print("Enter the elements and to stop press q.")
        #prompting the user again and again to enter the value in the list
        while True:
            #adding the value in the list
            weights.append(int(input())) 
                  
    #if input is not-integer, handling the exception by printing the list 
    except:
        #to handle repeted value convert into set
        weights = set(weights)
        weights = list(weights)
        print(weights)

    #prompting user to enter the desired weight
    desired_weight = int(input('Enter the desired weight '))
    #two variables to find the closes weight
    closes_weight = None
    actual_weight = None

    #loop to iterate over the weights set
    for i in range(0, len(weights)):
        #taking difference of each number in the weightset using abs to print positive value
        difference = abs(weights[i] - desired_weight)
        #the first element is set to actual weight by default 
        if i == 0:
            closes_weight = difference
            actual_weight = weights[i]
            continue
        #number closest to the given set but not greater than the desired weight
        if difference < closes_weight:
            closes_weight = difference
            actual_weight = weights[i]
            
    #removing the closest number
    weights.remove(actual_weight)
    print('Resulting set is ', weights)
    print('Actual weight is:', actual_weight)


if __name__=='__main__':
        main()

def main():
    """
        Main function
    """
    #Declaring and initializing lists
    boysList = []
    girlsList = []

    #try and except to handle exception
    try:
        #Reading data from the files
        boysFile = open("BoyNames.txt", "r")
        girlsFile = open("GirlNames.txt", "r")
        #Adding the names in their respective list
        for Boysname in boysFile:
            boysList.append(Boysname.strip()) #strip to remove whitespaces before or after
        #Adding girls names
        for Girlsname in girlsFile:
            girlsList.append(Girlsname.strip()) #strip to remove whitespaces before or after

    #error due to wrong directory name or file doesn't exist 
    except FileNotFoundError:
        print('Files does not exists or check you path.')

    choice = ""
    
    #asking again and again until user enters quit
    #while(choice != "quit"):

        
    #promting user for the input
    choice = str(input("Choose: girl / boy / both / quit : ")).casefold() #casefold to convert into lowercase even when input is uppercase

    #If girl's name is selected
    if choice == "girl":
        #Asking the girl name
        girlsName = input("Input a girl name: ")

        #Finding the name in the girl list
        if girlsName in girlsList:
            #If present
            print(girlsName + " was a popular girl's name between 2000 and 2009, at index",(girlsList.index(girlsName))+1) #index to get the index number of the list
            print("\n")
        else:
            #Not there
            print(girlsName + " was not a popular girl's name between 2000 and 2009.\n")

    #If boy's name is selected
    elif choice == "boy":
        #Asking the boy name
        boysName = input("Input a boy name: ")

        #Finding the name in the boy list
        if boysName in boysList:
            #If present
            print(boysName + " was a popular boy's name between 2000 and 2009, at index",(boysList.index(boysName))+1) #index to get the index number of the list
            print("\n")
        else:
            #Not there
            print(boysName + " was not a popular boy's name between 2000 and 2009.\n")

    # Searching for both
    elif choice == "both":
        #Asking the boy name
        boysName = input("Input a boy name: ")

        #Finding the name in the boy list
        if boysName in boysList:
            #If present
            print(boysName + " was a popular boy's name between 2000 and 2009, at index",(boysList.index(boysName))+1) #index to get the index number of the list
            print("\n")
        else:
            #Not there
            print(boysName + " was not a popular boy's name between 2000 and 2009.\n")
                
        #Asking the girl name
        girlsName = input("Input a girl name: ")

        #Finding the name in the girl list
        if girlsName in girlsList:
            #If present
            print(girlsName + " was a popular girl's name between 2000 and 2009, at index",(girlsList.index(girlsName))+1) #index to get the index number of the list
            print("\n")
        else:
            #Not there
            print(girlsName + " was not a popular girl's name between 2000 and 2009.\n")
        
             
    else:
        print("\n Invalid selection.... \n")
      
# Calling main function      
if __name__ == "__main__":
    main()

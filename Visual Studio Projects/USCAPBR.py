def main():
    #dictionary with state as the key and the list as value containing the capitals and birds
    """NESTED LIST First Element OF EVERY LIST IS THE STATE AND
       SECOND ELEMENT IS THE LIST WHOSE FIRST ELEMENT IS CAPITAL AND SECOND IS BIRD
    """
    US = [
    ['New Hampshire',['Concord','Purple Finch']],
    ['New Jersey',['Trenton','Eastern Goldfinch']],
    ['New Mexico',['Santa Fe','Roadrunner']],
    ['New York',['Albany','Bluebird']],
    ['Alabama',['Montgomery','Yellowhammer']],
    ['Alaska',['Juneau','Willow Ptarmigan']],
    ['Arizona',['Phoenix','Cactus Wren']],
    ['Arkansas',['Little Rock','Mockingbird']],
    ['California', ['Sacramento','Valley Quail']],
    ['Colorado',['Denver','Lark Bunting']],
    ['Connecticut',['Hartford','Robin']],
    ['Delaware',['Dover','Blue Hen']],
    ['Florida',['Tallahassee','Mockingbird']],
    ['Georgia',['Atlanta','Brown Thrasher']],
    ['Hawaii',['Honolulu','Nene']],
    ['Idaho',['Boise','Mountain Bluebird']],
    ['Illinios',['Springfield','Cardinal']],
    ['Indiana',['Indianapolis','Cardinal']],
    ['Iowa',['Des Monies','Eastern Goldfinch']],
    ['Kansas',['Topeka','Western Meadowlark']],
    ['Kentucky',['Frankfort','Cardinal']],
    ['Louisiana',['Baton Rouge','Eastern Brown Pelican']],
    ['Maine',['Augusta','Chickadee']],
    ['Maryland',['Annapolis','Baltimore Oriole']],
    ['Massachusetts',['Boston','Chickadee']],
    ['Michigan',['Lansing','Robin']],
    ['Minnesota',['St. Paul','Common Loon']],
    ['Mississippi',['Jackson','Mockingbird']],
    ['Missouri',['Jefferson City','Bluebird']],
    ['Montana',['Helena','Western Meadowlark']],
    ['Nebraska',['Lincoln','Western Meadowlark']],
    ['Neveda',['Carson City','Mountain Bluebird']],
    ['Ohio',['Columbus','Cardinal']],
    ['Oklahoma',['Oklahoma City','Scissor-Tailed Flycatcher']],
    ['Oregon',['Salem','Western Meadowlark']],
    ['Pennsylvania',['Harrisburg','Ruffed Grouse']],
    ['Rhoda Island',['Providence','Rhode Island Red']],
    ['Tennessee',['Nashville','Mockingbird']],
    ['Texas',['Austin','Mockingbird']],
    ['Utah',['Salt Lake City','California Seagull']],
    ['Vermont',['Montpelier','Hermit Thrush']],
    ['Virginia',['Richmond','Cardinal']],
    ['Washington',['Olympia','Willow Goldfinch']],
    ['Wisconsin',['Madison','Robin']],
    ['Wyoming',['Cheyenne','Western Meadowlark']],
    ['West Virginia',['Charleston','Cardinal']],
    ['South Carolina',['Columbia','Great Carolina Wren']],
    ['South Dakota',['Pierre','Ring-Necked Pheasant']],
    ['North Carolina',['Raleigh','Cardinal']],
    ['North Dakota',['Bismarck','Western meadowlark']],
    ['District of Columbia',['Washington D.C.','Wood Thrush']],
    ]
    
    #menu creation
    #creating the menu
    while (True):
        print("\n1.Display all U.S. States with their Capitals and Birds.")
        print("2.Search State for their Capital and Bird.")
        print("3.Update Bird for State.")
        print("4.Exit.")
    
        
        #prompting the user for the choice
        choice = str(input("Make a choice : "))

        #when choice is 1
        if (choice == "1"):
            US.sort() #sorting the function that is used to sort the list alphabetically

            #loop to iterate over and print the result
            for i in range (0,len(US)):
                #printing the result
                print("State: " + US[i][0] + ", Capital: " + US[i][1][0] + ", Bird: " + US[i][1][1])

        #on choice 2
        elif (choice == "2"):
            #prompt user for state input
            state = str(input("Please enter the state name: "))
            
            #loop to iterate over the list
            for i in range (0,len(US)):
                #finding the state in the list first lement
                if state == US[i][0]:
                    print("Capital: " + US[i][1][0] + "\nBird: " + US[i][1][1])
                    break
            #if the state name is wrong
            else:
                print("Please check your state.")

        #for choice 3
        elif (choice == "3"):
            #prompt user for state input
            state = str(input("Please enter the state name: "))
            
            #loop to iterate over the list
            for i in range (0,len(US)):
                #finding the state in the list first lement
                if state == US[i][0]:
                    #prompting user for the new bird name
                    bird = str(input("Please enter the new bird name: ")).capitalize()
                    #updating the bird
                    US[i][1][1] = bird
                    break
            #if the state name is wrong
            else:
                print("Please check your state.")

        #if choice is 4
        elif (choice == "4"):
            #quitting the program
            break

        #to check the wrong input
        else:
            print("Wrong Input.")


if __name__ == "__main__":
    main()




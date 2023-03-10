##calling all the essential libraries
import pandas as pd
import numpy as np
import re

#creating the main function
def main():
    data = [
        ['Jim', 'Robertson', '21801', '555-555-5555'],
            
        ['John', 'Adams', '223211143', '4444444444'],
                    
        ['Helen', 'Cooper', 'edskd-2134','323232'],
                    
        ['Franklin', ' ', '234511', '323-333-2211'],

        ['', 'Philips', 'asada-46016', '8123049340'], ##taken this one extra to check all conditions

        ]


    #iterating over the rows
    for person in data:
        #iterating over the columns
        for row in data:
            #case when the name is not alphabets 
            if not re.match(r"^[A-Z][a-z]+$", person[0]):
                #set name as empty string
                person[0] = ""
            #case when the name is not alphabets 
            if not re.match(r"^[A-Z][a-z]+$", person[1]):
                #set name as empty string
                person[1] = ""
            #case if the character is alpha numeric or not.
            if not row[0].isalpha():
                #for that case also string set empty
                row[0] = ''
            if not row[1].isalpha():
                #for that case also string set empty
                row[1] = ''
            #removing the slashes to count the character from the zip code and the phone number
            if not row[2].replace('-', '').isdigit():
                row[2] = ''
            #removing the slashes to count the character from the zip code and the phone number
            if not row[3].replace('-', '').isdigit():
                row[3] = ''
                
            if row[2] is not '':
                # removing '-' from string i.e zip code
                row[2] = re.sub(r'\D', '', row[2])
                
            #case when zip code's length is 9    
            if len(row[2]) == 9:
                #slicing to add dashes
                row[2] = row[2][:5] + '-' + row[2][5:]
            #case when the length is 5
            elif len(row[2]) == 5:
                #left as it is
                pass # doing nothing
            #for other cases
            else:
                #column is set with empty records
                row[2] = ''
            #checking whether the phone number is empty or not
            if row[3] is not '':
                # removing '-' from string i.e phone number
                row[3] = re.sub(r'\D', '', row[3])
            #checking the length of the phone number if it is 10 then fine
            if len(row[3]) == 10:
                #slicing to add dashes
                row[3] = row[3][:3] + '-' + row[3][3:6] + '-' + row[3][6:]
            #otherwise setting the records for 
            else:
                #records are set to empty
                row[3] = ''


    #reading the 2D list as the dataframe
    people_df = pd.DataFrame(data, columns=["Firstname", "Lastname", "Zipcode", "Phone"])

    #printing the result without index
    print(people_df.to_string(index=False))

#calling the function
if __name__ == '__main__':
    main()

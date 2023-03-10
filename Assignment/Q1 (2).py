##def strLength(myStr):
##
##   if myStr == '':
##
##       return 0
##
##   else:
##
##       return 1 + strLength(myStr[1:])
##
##print(strLength("13 characters"))


##
##def linear(string_list, search_string):
##    counter = 0
##    end_of_list = len(string_list)
##    result = [] #//empty list to hold the index
##    flag = True #//to check whether the result is true
##    for i in range(0, end_of_list): #//for i in range(0, (end_of_list + 1)): running loop out of index
##        try:
##            if string_list[i] == search_string:
##                result.append(i) #//add the values as index in list
##                counter += 1
##            elif len(result) == 0:
##                flag = False
##        except IndexError as e:
##            return "error"
##    return result , flag #//return the flag and the result list 
##
##
##
##print(linear(["bob","burgers","tina","bob"],"bob"))
##
##print(linear(["bob","burgers","tina","bob"],"bae"))
##
##print(linear(["bob","bobby","bob"],"bob"))
##
##





from datetime import date
# Function is used to perform recursive binary search
def binary_search_year(searchList, searchTerm):
    # sorting the list of dates
    searchList.sort()
    low = 0
    high = len(searchList)
    if len(searchList) == 0:
       return False
    if low<=high and high>0:
        # finding 'mid' index to compare the values
        mid = int((low+high)/2)
        # checking if 'mid' index contains the year value same as yr
        if searchTerm==searchList[mid].year:
            #print(listOfDates[mid].year, ' at location: ',mid )
            # if this is true 'True' is returned
            return True
        # if yr is lesses than year value at 'mid' index,
        elif searchTerm<searchList[mid].year:
            leftList = searchList[:mid-1]
            #then check for the left hand side sub list for 'yr' recursively
            return binary_search_year(leftList, searchTerm)
        else:
            rightList = searchList[mid+1:]
            #then check for the right hand side sub list for 'yr' recursively
            return binary_search_year(rightList, searchTerm)
        # return false otherwise
        return False

listOfDates=[date(2016,11,26), date(2014,11,29), date(2008,11,29), date(2000,11,25), date(1999,11,27), date(1998,11,28), date(1990,12,1), date(1989,12,2), date(1985,11,30)]
# required function call
print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))





##def binary_search_year(searchList, searchTerm):
##
##    searchList.sort()
##
##    if len(searchList) == 0:
##        return False
##
##    middle = len(searchList) // 2
##
##    if searchList[middle].year == searchTerm:
##        return True
##
##    elif searchTerm < searchList[middle].year:
##        return binary_search_year(searchList[:middle], searchTerm)
##
##    else:
##        return binary_search_year(searchList[middle + 1:], searchTerm)
##
##
##
##listOfDates=[date(2016,11,26), date(2014,11,29), date(2008,11,29), date(2000,11,25), date(1999,11,27), date(1998,11,28), date(1990,12,1), date(1989,12,2), date(1985,11,30)]
### required function call
##print(binary_search_year(listOfDates, 2016))
##print(binary_search_year(listOfDates, 2007))
##

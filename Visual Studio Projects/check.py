def main():

    inFile = open ("hidden.txt", 'r')
    outFile = open ("found.txt", 'w')
    count = 0
    first_line = inFile.readline()
    inFile.readline()
    
    first_line1 = first_line.split()
    
    width = int(first_line1[0])
    height = int(first_line1[-1])
    grid =[[] * height for i in range(width)]
    i = 0
    
    while True:
        firstGrid = inFile.readline()
        if firstGrid == '\n':
            break
        else:
            firstGrid = firstGrid.replace('\n', '')
            firstGrid = firstGrid.split()
            grid[i] = firstGrid
            i = i + 1
    inFile.readline()
    inFile.readline()
    word_list = []
    while True:
        wordList = inFile.readline()
        if wordList == '':
            break
        else:
            word_list.append(wordList.replace('\n', ''))
    print (word_list)
    print(grid)
    for row in grid[0]:
        if row in word_list:
            print ("true")
        else:
            print ("false")

    inFile.close()
    outFile.close()

main()

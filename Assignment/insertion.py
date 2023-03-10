def inserstionsort(lit):
    holepos = 0
    valueinst = 0

    for i in range (0,len(lit)):
        valueinst = lit[i]
        holepos = i

        while(holepos > 0 and lit[holepos-1] > valueinst):
            lit[holepos] = lit[holepos - 1]
            holepos = holepos - 1

        lit[holepos] = valueinst

    return lit

arr = [12, 11, 13, 5, 6] 
print(inserstionsort(arr))
            

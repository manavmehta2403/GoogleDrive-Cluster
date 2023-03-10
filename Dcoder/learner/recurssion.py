def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)


print(fact(4))



#FIBONNACI SERIES 0 1 1 2 3 5 8

def fibo(n):
    if (n >= 0):
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            return fibo(n-1) + fibo(n-2)

print(fibo(9))




##a = 0
##b = 1
##print(a)
##print(b)
##for i in range (0,5):
##    temp = a+b
##    a = b
##    b = temp
##    print(temp)

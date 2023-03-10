def isPrime(n, i = 2): 

    # Base cases 
    if n <= 1:
        return Exception("Neither composite nor prime.")
    else:
        if (i  >= n): 
            return 1 
        else:
            if (n == 2):
                return 1
            elif (n % i) == 0:
                return 0
            else:
                return isPrime(n,i+1)
    return 0

    
print(isPrime(-5))

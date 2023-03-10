num = 256
result = ""
while num > 0:
    result = str(num%2) + result
    num = num // 2
print(result)

bit = "100000000"
bit = int(bit)
result = ""
i = 0
while bit > 0:
    result = str(num%10) + str(2**i)
    bit = bit // 10
    i = i + 1
print(result)
    

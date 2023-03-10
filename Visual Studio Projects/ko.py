alphabet = []
for letter in range(65,123):
    if letter in range(91,97):
        continue
    alphabet.append(chr(letter))
print(alphabet)

num = int(input())
if num < 0:
    flag = True
    num = abs(num)
else:
    flag = False
result = ""
if num == 0:
    result = "0"
while (num > 0):
    result = str(num%2)+result
    num = num//2
if flag:
    result = "-" + result

print(result)

binary = 100 
decimal, i, n = 0, 0, 0
while(binary != 0): 
    dec = binary % 10
    decimal = decimal + dec * pow(2, i) 
    binary = binary//10
    i += 1
print(decimal)   

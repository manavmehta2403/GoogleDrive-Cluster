#python 2.7.6

print ("Hello, Dcoder!")
a=int(input("enter the number \n"))
reverse=0
while(a!=0):
 rem=a%10
 reverse=reverse*10+rem
 a=a//10
print(reverse)
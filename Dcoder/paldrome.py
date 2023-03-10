a=int(input("enter the number"))
rev=0
temp=a
while(a!=0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
if (rev==temp):
  print("palandrome")
else:
  print("chlna")

   

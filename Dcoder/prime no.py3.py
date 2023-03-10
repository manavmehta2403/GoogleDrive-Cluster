#python 3.6
print ("Hello, Dcoder!")
a=int(input("enter the no \n"))
f=0
if (a>1):
 for i in range(2,a):
  if (a%i==0):
    f=f+1
   
 if(f==0):
  print("prime")
 else:
  print("not prime")
else:
 print ("chlna")

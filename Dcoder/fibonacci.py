a=int(input("enter the number"))
x=0
y=1
print (x)
print(y)
for i in range(1,a):
    z=x+y
    x=y
    y=z
    print(z)

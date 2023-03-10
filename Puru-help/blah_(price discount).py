
##prompt for price input
price= int(input("enter the price: "))
#variable to store discount price
discount_price = 0

##check if price is greater than 1000
if price > 10000:
    ##then discount percentage is 30%
    print("discount is 30%")
    ##calculating discount price for 30%
    discount_price = price * (30/100)
    
elif price >5000:
    print("discount is 20%")
    discount_price = price * (20/100)
    
else:
    print("discount is 10%")
    discount_price = price * (10/100)

print("Your discount price is:",discount_price)

total = price - discount_price

print("Total cost:",total)

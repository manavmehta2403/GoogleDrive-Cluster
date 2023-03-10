#Ch - 3

#Q1 & Q2
try: 
  ##prompt user for the hours value
  hours = float(input("Please enter hours: "))
  ##prompt user for the rate value
  rate = float(input("Please enter rate: "))

  ##condition when hours is more than 40
  if ( hours > 40 ):
    ##calculating the number of hours left
    left_hours = hours - 40
    ##generating the pay for 40 hours + 1.5 * (40 - total hours)
    pay = (40 * rate) + (left_hours * (rate * 1.5))
    ##dsiplaying the output
    print("Pay:",pay)

  else:
    ##calculate payment using the formula hours * rate
    pay = hours * rate
    ##dsiplaying the output
    print("Pay:",pay)
    
#to catch any exception
except:
  print("Some values are enter were wrong!!!.")


#Q3
try:
  #prompt user to enter the score
  score = float(input("Please enter the score between (0.0 to 1.0): "))

  ##marking the range of the score
  if (score < 0.0 or score > 1.0):
    print("Score is out of range.")
  ## useing nested conditional statements for grading
  else:
    ##grading ruberics
    if (score >= 0.9):
      print("Grade: A")
    elif (score >= 0.8):
      print("Grade: B")
    elif (score >= 0.7):
      print("Grade: C")
    elif (score >= 0.6):
      print("Grade: D")
    else:
      print("Grade: F")

##catching any exception
except:
  print("Bad Score.")

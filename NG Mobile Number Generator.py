# My Nigeria mobile number generator in python
import random
print ("This program lets you generate nigerian phone numbers")
myNumbers = int(input("Enter the total numbers you want:" ))
for x in range(myNumbers):
  print ("080",(random.randint(10000000,99999999)))
print ("that is all the numbers you requested!")

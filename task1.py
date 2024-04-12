#!python3
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""



import math
p = float(input("Enter your amount of principal: "))
r = float(input("Now enter the rate of interest as a percentage:  "))
t = float(input("Enter the number of days in the month:  "))
t = t/365
i = float

i = p * r * t 

a = round(i,2)
print(f"You earned ${a} interest")
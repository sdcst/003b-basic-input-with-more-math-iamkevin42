#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

a = float(input("Enter your first item\n"))
b = float(input("Enter your second item\n"))
c = float(input("Enter your third item\n"))
d = float(input("Enter your fourth item\n"))
e = float(input("Finally enter your last item\n"))


total = a + b + c + d + e 
tax = total * 0.12
roundedtax=round(tax,2)
totaltotal = tax + total
roundedtotaltotal=round(totaltotal, 2)

print(f"Your subtotal is {total} and your taxes total to {roundedtax} for a total of {roundedtotaltotal}")
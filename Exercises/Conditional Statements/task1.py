""" Write a program that takes an integer as input and prints whether it is positive, negative, or zero.
Write your program below
"""

#!/usr/bin/python3
""" program that takes an integer as positve or negative."""
 
integer_num = int(input("Enter the value of your number\n"))

""" any number greater zero is positive.
    a number less than zero is negative otherwise zero
	"""

if integer_num > 0:
	print("your number is positive")
elif integer_num == 0:
	print("your number is zero")
else:
	print("your number is negative")
   


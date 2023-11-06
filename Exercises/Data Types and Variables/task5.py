#!/usr/bin/python3

#using conditional statement

age = int(input("Enter your age: "))
if age >= 0 and age < 18:
    print("you can't vote")
elif age == 18:
    print("Register for National identity card")
elif age > 18:
    print("You are eligible to vote and Drink thereafter")
else:
    print("Not yet born")

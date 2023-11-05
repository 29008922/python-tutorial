#!/usr/bin/python3
# Write a Python program that converts Fahrenheit temperatures to Celsius temperatures.
# The program should ask the user to enter a temperature in Fahrenheit,and then print the
# equivalent temperature in Celsius.The conversion formula is: C = (F - 32) * 5/9
# write your program below

#conversion of farein height to tempereature in 0C

Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5/9
print('%.2f F = %.2f 0C ' %(Fahrenheit, Celsius))

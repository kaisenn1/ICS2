'''
Name: Kaisen
Date: November 1, 2021
Program Name: inches to centimeters display
Description: There are 2.54 cm in one inch. Write a program to enter the length of a
door in inches and output its length in centimetres. Use a constant for the
conversion factor. Be sure prompt for the input and to label the output.
'''

n = input("Enter value in inches to convert to centimeters: ")
cm = 2.54
try:
    n = int(n)
    ncm = n * cm
    print(n,'inches is',ncm,'centimeters')
except:
    print('Input(s) may not be a number')
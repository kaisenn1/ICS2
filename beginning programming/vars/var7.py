'''
Name: Kaisen
Date: November 1, 2021
Program Name: n5 display
Description: Ask the user for any number. Print five times the number.
'''

n = input("Enter number to be multiplied by 5: ")
try:
    test = int(n)
    print(test * 5)
except:
    print('Input(s) may not be a number')
'''
Name: Kaisen
Date: November 1, 2021
Program Name: n1 * n2 display
Description: Write a program that asks the user for two numbers. Multiply them
together and print the result.
'''


n, n1 = input("Enter two numbers to be multiplied, seperated by a space: ").split()
try:
    n = float(n)
    n1 = float(n1)
    print(n * n1)
except:
    print('Input(s) may not be a number')
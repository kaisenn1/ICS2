'''
Name: Kaisen
Date: November 1, 2021
Program Name: arithmetic functions display
Description: Write a program that will ask users to input 2 integers and then output the
sum, difference, product, and quotient.
'''

print("Enter two numbers to find sum, difference, product, and quotient, seperated by a space ")
n = input('Enter the first number: ')
n1 = input('Enter the second number: ')
try:
    n = int(n)
    n1 = int(n1)
    sum = n + n1
    difference = n1 - n
    product = n * n1
    quotient = n1 / n
    print('Sum =',sum,'\nDifference =',difference,'\nProduct =',product,'\nQuotient =',quotient)
except:
    print('Input(s) may not be a number')
'''
Name: Kaisen
Date: November 1, 2021
Program Name: interest calculator
Description: You are investing money (principal) for a certain rate (%) for a number of
years (time). Write a program that calculates the interest you would earn.
Be sure to round the amount to the nearest cent.
'''

print('Investment calculator 3000')
try:
    p = float(input('Enter money to be invested (Principal): '))
    r = float(input('Enter interest rate (Percentage as a decimal, etc: 0.x): '))
    t = int(input('Enter expected money storage time (Years): '))
    i = p * t * r
    print('Estimated interst: $',round(i, 2))
except:
    print('Invalid input')
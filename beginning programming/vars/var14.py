'''
Name: Kaisen
Date: November 1, 2021
Program Name: radius to circumference
Description: Have the user enter the radius of a circle (accurate to two decimals) and
output the circumference (accurate to three decimal places).
'''

import math

c = float(input('Enter radius to find circumference (to 2 decimals): '))
x = round(c, 2)
if x == c:
    c = 2 * math.pi * c #slight change, circumference formula is actually 2piR
    cn = round(c, 3)
    print('Circumference = ',cn)
else:
    print('Exceeding decimal limit')
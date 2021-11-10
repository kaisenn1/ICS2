'''
Name: Kaisen
Date: November 1, 2021
Program Name: mark to percentage display
Description: Ask the user for a subject, the total number of marks in a test, and their
test mark. Calculate their test mark as a percent to one decimal place and
output the result.
'''

s = input('Enter academic subject: ')
try:
    t = int(input('Enter total available marks: '))
    a = int(input('Enter actual mark: '))
    x = a / t * 100
    rounded = round(x, 1)
    print(s + ',',rounded,'%')
except:
    print('Input(s) may not be a number')
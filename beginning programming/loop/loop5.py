# Name Kaisen
# Date November 8, 2021
# Title Loop5
# Description endlessly asks and finds the sum of an infinite amount of numbers

import time

true = True
y = False
print('Please enter a number, followed by another(s) to find the total sum')
time.sleep(0.5)
while (true):
    x = int(input('Please enter a number: '))
    if y == False:
        y = 0
        print('The value is',x)
        y = x
        z = x
    else:
        z = x + y
        print('The total sum is', z)
        y = z


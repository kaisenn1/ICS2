#Name Kaisen
#Date Novemeber 16, 2021
#Title for5
# Description asks and finds the sum of an infinite amount of numbers 5 times

import time

y = False
print('Please enter a number, followed by another(s) to find the total sum')
time.sleep(0.5)
for i in range(5):
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


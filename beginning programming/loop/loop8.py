# Name Kaisen
# Date November 8, 2021
# Title Loop6
# Description

true = True
while (true):
    n = int(input('Please enter  a number: '))
    if n < 0:
        true = False
        exit('Negative number!!!')
    print(n, 'squared is:', n * n)


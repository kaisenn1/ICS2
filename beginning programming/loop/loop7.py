# Name Kaisen
# Date November 8, 2021
# Title Loop6
# Description

true = True
while (true):
    l = int(input('Please enter the length: '))
    w = int(input('Please enter the width: '))
    if l < 0:
        true = False
        exit('Invalid length')
    print(l * w)


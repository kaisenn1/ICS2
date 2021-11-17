# Name Kaisen
# Date November 8, 2021
# Title Loop7
# Description endlessly asks for length and width to find area until inputted length is negative

true = True
while (true):
    l = int(input('Please enter the length: '))
    w = int(input('Please enter the width: '))
    if l < 0:
        true = False
        exit('Invalid length')
    for i in range(5): #calculates area 5 times
        print(l * w)


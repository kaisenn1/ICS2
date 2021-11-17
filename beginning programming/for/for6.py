#Name Kaisen
#Date Novemeber 16, 2021
#Title for6
# Description  asks for length and width to find area until inputted length is negative 4 times

true = True
while (true):
    l = int(input('Please enter the length: '))
    w = int(input('Please enter the width: '))
    if l < 0:
        true = False
        exit('Invalid length')
    for i in range(5): #calculates area 5 times
        print(l * w)


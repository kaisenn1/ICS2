#Name Kaisen
#Date Novemeber 8, 2021
#Title String8
#Description asks user to enter up to 5 names, program ends if 5 names is reached or end is typed

count = 0
while count < 5:
    names = input('Please enter names, to a maxiumum of 5: ')
    count += 1
    if count == 5 or names == 'end':
        break


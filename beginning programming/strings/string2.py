#Name Kaisen
#Date Novemeber 8, 2021
#Title String2
#Description

count = 0
while (True):
    names = input('Please enter student name: ')
    if names == 'quit':
        print(count, 'students')
        break
    count += 1

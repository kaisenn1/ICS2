#Name Kaisen
#Date Novemeber 8, 2021
#Title String3
#Description

count = 0
true = True
while (true):
    names = input('Please enter student name: ')

    if names == 'quit':
        print(count, 'students')
        break

    count += 1
    print(count, 'students')
#Name Kaisen
#Date Novemeber 8, 2021
#Title String3
#Description prints amount of students after every student name entry

count = 0
while (True):
    names = input('Please enter student name: ')

    if names == 'quit':
        print(count, 'students')
        break

    count += 1
    print(count, 'students')
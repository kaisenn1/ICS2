#Name Kaisen
#Date Novemeber 8, 2021
#Title String10
#Description asks user to enter integer, if word quit is entered and integer is greater than or equal to 10 , program ends


while (True):
    number = input('Please enter a integer: ')
    if number == 'quit':
        numbers = int(input('Please enter a integer greater than or equal to 10: '))
        if numbers >= 10:
            break
        continue


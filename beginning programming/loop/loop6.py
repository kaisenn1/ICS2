# Name Kaisen
# Date November 8, 2021
# Title Loop6
# Description endlessly asks for a name and number until a negative number is inputted

true = True
while (true):
    n = input('Please enter your name: ')
    a = int(input('Please enter a number: '))
    if a > 0:
        true = True
    if a < 0:
        true = False
exit('Negative number!!!')

#Name Kaisen
#Date Novemeber 8, 2021
#Title String7
#Description asks user to enter up to 5 words, once limit is reached or word stop is entered, program terminates

count = 0
while count < 5:
    word = input('Please enter word: ')
    count += 1
    if count == 5 or word == 'stop':
        break
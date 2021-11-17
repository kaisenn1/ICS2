# Name Kaisen
# Date November 8, 2021
# Title Loop13
# Description asks for a word, asks for how many times to print word, prints word x times, with line numbers in front

x = input('Please enter a word: ')
n = int(input('Please enter amount of time(s) to be printed: '))
for i in range(n):
    print("%d." % i,x)




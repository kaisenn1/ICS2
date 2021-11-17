# Name Kaisen
# Date November 8, 2021
# Title Loop13
# Description outputs total sum from numbers 5 to 15

y = 0
for i in range(5, 16):
    if y == 0:
        print('The total sum is',i)
        y = i
        z = i
    else:
        z = i + y
        print('The total sum is', z)
        y = z





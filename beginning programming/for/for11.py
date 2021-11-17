#Name Kaisen
#Date Novemeber 16, 2021
#Title for11
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





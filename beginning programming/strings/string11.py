#Name Kaisen
#Date Novemeber 8, 2021
#Title String8
#Description


x = 0
while (True):
    x += 1
    print('Loop execution number', x)
    more = input("Type 'more' to continue: ")
    if more == 'more':
        continue
    elif more == 'stop':
        break

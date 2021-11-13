#Name Kaisen
#Date Novemeber 8, 2021
#Title String11
#Description prints loop execution number then requests user permission to continue loop


x = 0
while (True):
    x += 1
    print('Loop execution number', x)
    more = input("Type 'more' to continue: ")

    if more == 'more':
        continue
    elif more != 'more':
        print("Not 'more'")
        break
    elif more == 'stop':
        break
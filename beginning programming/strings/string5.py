#Name Kaisen
#Date Novemeber 8, 2021
#Title String5
#Description asks for subject and mark, prints average mark if quit is entered

average = 0
totalmarks = 0
def marks():
    nonround = average / totalmarks
    print(round(nonround, 2))
while (True):
    subject = input("Enter subject: ")
    if subject == 'quit':
        marks()
        break

    mark = input("Enter mark: ")
    if mark == 'quit':
        marks()
        break
    marki = int(mark)
    totalmarks += 1
    average += marki


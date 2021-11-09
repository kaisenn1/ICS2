# Name Kaisen
# Date November 8, 2021
# Title Loop16
# Description asks for total amount of marks then asks for individual mark, total amount of marktimes

totalmarks = int(input('Please enter the total number of marks: '))
x = 1
totalmark = 0
for i in range (totalmarks):
    mark = int(input('Please enter mark {}: '.format(x)))
    x += 1
    totalmark += mark
average = totalmark / totalmarks
print('The average of ', totalmarks,' marks is ', average)

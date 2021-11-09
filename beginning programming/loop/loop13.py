# Name Kaisen
# Date November 8, 2021
# Title Loop13
# Description prints numbers 1 to 15 then prints the total sum

count = 1
x = 0
while count <= 15:
    print(count)
    x += count
    count += 1

print('The sum of the numbers from range 1-15 is', x)
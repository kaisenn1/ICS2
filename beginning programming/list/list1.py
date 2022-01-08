#Name Kaisen
#Date January 7, 2022
#Title list1
#Description asks for ages, then inputs ages above average
'''
pseudocode
set lists for ages and ages above average
ask for total number of ages
ask for age x times, where x is the number of ages inputted
calculate average by dividing sum / number of ages
calculate ages above average by checking if items in list are greater than the average
print average age sorted least to greatest
'''

ages = [] #sets list of ages for input
aboveages = [] #sets list ofages that are greater than average
totalages = int(input('Please input the total amount of ages: ')) #sets total number of ages
for i in range(totalages):
    age = int(input('Please input age: '))
    ages.append(age)
average = sum(ages) / len(ages) #finds average by dividing ages by number of ages
for item in ages:
    if item > average: #checks if age is above average, if true, then add age to 'aboveages' list
        aboveages.append(item)
print('Average age is:', average)
print('Ages above average are:', sorted(aboveages)) #prints ages sorted from lowest to greatest

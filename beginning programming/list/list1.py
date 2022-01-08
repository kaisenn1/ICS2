'''
Name: Kaisen
January 7, 2022
Title: list1
Description: asks for heights, then output heights above average
---
pseudocode:
set lists for heights and heights above average
ask for total number of heights
ask for height x times, where x is the number of heights inputted
calculate average by dividing sum / number of heights
calculate heights above average by checking if items in list are greater than the average
print average height sorted least to greatest
'''

heights = [] #sets list of heights for input
aboveheights = [] #sets list of heights that are greater than average
totalheights = int(input('Please input the total amount of heights: ')) #sets total number of heights
for i in range(totalheights):
    height = int(input('Please input height in centimeters: '))
    heights.append(height)
average = sum(heights) / len(heights) #finds average by dividing heights by number of heights
for item in heights:
    if item > average: #checks if height is above average, if true, then add age to 'aboveheights' list
        aboveheights.append(item)
print('--- Average height is', average, 'cm ---')
print('Heights above average are:', sorted(aboveheights)) #prints heights sorted from lowest to greatest

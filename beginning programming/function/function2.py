#Name Kaisen
#Date December 14, 2021
#Title function2
#Description gallons per mile ratio calculator

'''
pseudocode:
set litre to gallon ratio
ask for litres consumes
ask for miles drive
calculate litres to gallons
calculate miles / gallons
    return answer
print answer
'''

LITRE = 0.264179

def calccost(litres, miles):
    gallons = litres * LITRE #calculates gallons
    ratio = miles / gallons #calculates gallon to mile ratio
    return ratio

litres = int(input('How many litres of fuel have been consumed?: '))
miles = int(input('How many miles has been driven?: '))
print('Miles Per Gallon is:', round(calccost(litres,miles),2)) #prints and executes rounded function result
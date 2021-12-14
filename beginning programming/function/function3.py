#Name Kaisen
#Date December 10, 2021
#Title function1
#Description
'''
Pseudocode:
get current rate
ask for which currency to convert to
ask for amount to be converted
pass amount in function corresponding for currency to convert to
    return value
print value of amount converted into currency
'''

def convert_FEET(feet):               #converts usd to cad
    value = 0.3048 * feet
    return value

def convert_INCH(inches):              #converts cad to usd
    value = inches * 2.54
    return value

def start():
    feet = int(input('Please enter amount of feet: : '))
    inches = int(input('Please enter amount of inches: : '))
    convert_FEET(feet)
    convert_INCH(inches)

start()

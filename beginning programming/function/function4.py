#Name Kaisen
#Date December 14, 2021
#Title function4
#Description asks for feet and inches, converts to meters and centimeters
'''
Pseudocode:
ask for feet
ask for inches
convert feet to meters + cm
convert inches to cm
return results
print results
'''

def convert_FEET(feet): #converts feet to meters and centimeters, before decimal point meter, after decimal point centimeter
    value = 0.3048 * feet
    return value

def convert_INCH(inches): #converts inches to centimeters
    value = inches * 2.54
    return value / 100 #divide by 100 to make it centimeters AFTER a decimal

def start():
    feet = int(input('Please enter amount of feet: '))
    inches = int(input('Please enter amount of inches: '))
    total = convert_FEET(feet) + convert_INCH(inches) #adds meters and inches
    print(str(round(total, 2))+ 'm') #prints result slightly rounded
start()

#answer seems to vary from this code to websites to websites
#asking google 5 feet 8 inches in cm results to 172.72
#https://www.google.com/search?client=safari&rls=en&q=5+feet+8+inches+in+cm&ie=UTF-8&oe=UTF-8
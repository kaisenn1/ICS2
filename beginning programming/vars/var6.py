'''
Name: Kaisen
Date: November 1, 2021
Program Name: Age display
Description: Ask the user to enter their age. Output their response.
'''

a = input("Enter current age: ")
try:
    # adding a error finder so users don't get confused when they accidently type a letter alongside a number
    test = int(a)
    print("You are " + a +" years young!")
except:
    print('Input(s) may not be a number')
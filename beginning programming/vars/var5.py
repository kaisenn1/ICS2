'''
Name: Kaisen
Date: November 1, 2021
Program Name: Address display
Description: Write a program that reads in an address of four lines: name, street, city
and province, and postal code and outputs this address all on one line with
commas between the parts.
'''

n = input("Enter name: ")
s = input("Enter street: ")
cp = input("Enter city and province: ")
pc = input("Enter postal code: ")

print(n +', ' + s + ', ' +cp + ', ' + pc)
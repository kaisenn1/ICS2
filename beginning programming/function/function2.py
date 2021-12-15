#Name Kaisen
#Date December 14, 2021
#Title function2
#Description

'''
pseudocode:
ask for weight
ask if special delivery is wanted
pass weight and if special delivery is wanted into function
calculate price of first gram + after first grame price * weight - 1
if not whole{
    add 35 cents
}
return price
'''

print('First-Class Letter Cost Calculator')
weight = float(input('Please enter envelope weight in grams: ')) #takes weight
special_delivery = input('Is special delivery required?(Yes/No): ') #takes answer

def calccost(weight, special_delivery):
    price = 1.05 + (0.35 * (round(weight) - 1)) #sets base price, then multiples gram cost by weight, removing 1 gram from weight because of inital cost
    if weight != round(weight): #tests if weight is rounded, if weight is not equal to its rounded version, it means it is a partial gram and needs cost added
        price += 0.35
    if special_delivery.lower() == 'yes': #converts to lowercase in case user types upercase
        price += 15
    return price

print('$' + str(round(calccost(weight,special_delivery), 2))) #executes function, then converts function response to string, to be concatnated with "$"
#Name Kaisen
#Date December 14, 2021
#Title function3
#Description displays current currency rates, asks what currency user would like to exchange too, then displayes exchanged value of inputed currency
'''
Pseudocode:
get current rate
ask for which currency to convert to
ask for amount to be converted
pass amount in function corresponding for currency to convert to
    return value
print value of amount converted into currency
'''

from forex_python.converter import CurrencyRates  #current exchange rate

rate = CurrencyRates()

def convert_rateUS(amount):               #converts usd to cad
    value = rate.convert('USD', 'CAD', amount)
    return value

def convert_rateCA(amount):              #converts cad to usd
    value = rate.convert('CAD', 'USD', amount)
    return value

def start():
    currency = input('Convert USD -> CAD OR CAD -> USD? [USD/CAD]: ')
    amount = int(input('How much money is to be converted?: '))
    if currency != 'USD': #if currency is not usd, then it must be CAD and runs CAD to usd
        print("$" + str(amount), "CAD exchanges to $" + str(round(convert_rateCA(amount),2)), "USD")
    else: #if it is USD, then converts USD to cad
        print("$" + str(amount), "USD exchanges to $" + str(round(convert_rateUS(amount),2)), "CAD")

print("Currency Exchange Rate Machine\n - Today's Rates -")
print('Current Rate Of 1 USD -> CAD Is:', convert_rateUS(1)) #current rates of USD to cad and vice versa
print('Current Rate Of 1 CAD -> USD Is:', convert_rateCA(1))
start()

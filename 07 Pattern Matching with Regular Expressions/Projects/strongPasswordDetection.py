# Strong Password Detection Program

import re

text = input("Enter your password : ")
# check for atleast one UPPERCASE
upperRegex = re.compile(r'([A-Z]+)')
try:
    upper = upperRegex.search(text).group()
except AttributeError:
    upper = ''
# check for atleast onr LOWERCASE
lowerRegex = re.compile(r'([a-z]+)')
try:
    lower = lowerRegex.search(text).group()
except AttributeError:
    lower = ''
# check for atleast one DIGIT
decimalRegex = re.compile(r'([0-9]+)')
try:
    decimal = decimalRegex.search(text).group()
except AttributeError:
    decimal = ''

# Validation
if(len(text) > 7 and upper != '' and lower != '' and decimal != ''):
    print('YES! Strong Password')
else:
    print('Yout password is not strong enough! TRY AGAIN !!!')

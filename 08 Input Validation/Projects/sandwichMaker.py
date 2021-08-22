# Sandwich Maker 
import pyinputplus as pyip

# Displays Bill in format of a table
def Tablebill(itemsPrice, selected, number):
    print('\n-------------------')
    print('Items'.ljust(11),'Price'.rjust(5))
    print('-------------------')
    totalCount = 0
    for item in selected :
        try:
            totalCount += itemsPrice[item]
            print(item.ljust(11), str(itemsPrice[item]).rjust(5))
        except:
            totalCount += 0
    print('-------------------')
    print('Total Count'.ljust(11),str(totalCount).rjust(5))
    print(('x ' + str(number)).rjust(17))
    print('-------------------')
    print('Bill'.ljust(5),str(totalCount*number).rjust(11))
    print('-------------------')


# Prices of items
itemsPrice = {'wheat':5, 'white':10, 'sourdough':15, 'chicken':5, 'turkey':10, 'ham':15, 'tofu':20,
              'cheddar':2, 'Swiss':4, 'mozzarella':8, 'mayo':1, 'mustard':2, 'lettuce':3, 'tomato':4}
selected = []

# Bread 
selected.append(pyip.inputMenu(['wheat', 'white', 'sourdough'], 
                numbered = True, prompt = 'Select type of bread you want : \n'))
# Protein
selected.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 
                numbered = True, prompt = 'Select type of protein you want : \n'))
# Cheese
cheese = pyip.inputYesNo(prompt = 'Do you want cheese?(Y/N) - ')
if(cheese == 'yes'):
    cheeseType = selected.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered = True))

# Others
if pyip.inputYesNo(prompt = 'Do you want mayo? - ') == 'yes' :
    selected.append('mayo')
if pyip.inputYesNo(prompt = 'Do you want mustard? - ') == 'yes' :
    selected.append('mustard')
if pyip.inputYesNo(prompt = 'Do you want lettuce? - ') == 'yes' :
    selected.append('lettuce')
if pyip.inputYesNo(prompt = 'Do you want tomato? - ') == 'yes' :
    selected.append('tomato')

# Total Sandwiches
number = pyip.inputInt(prompt = 'How many sandwiches do you want? - ', min = 1)

Tablebill(itemsPrice, selected, number)
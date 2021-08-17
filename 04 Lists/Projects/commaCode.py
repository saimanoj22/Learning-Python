# This is Comma Code Solution

def commaCode(list):
    str = ''
    for i, name in enumerate(list):
        if(i == len(list)-1):
            str += 'and ' + name
        else:
            str += name + ', '
    return str

spam = ['apples', 'bananas', 'tofu', 'cats']
#spam = []           # Empty List
print(commaCode(spam))
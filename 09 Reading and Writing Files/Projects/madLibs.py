# !python
# This is MAd Libs Program.
# This enables the user to open and read a file.
# It lets user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re
# opening file
file = open('.\Mad Libs Files\madLibs.txt')
fileContent = file.read()
file.close()
# program
print('Original Content:')
print(fileContent,'\n')
madRegex = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')
matches = madRegex.findall(fileContent)
for i in range(len(matches)):
    if matches[i].lower() == 'adjective':
        print('Enter an ' + matches[i].lower() + ':')
    else:
        print('Enter a ' + matches[i].lower() + ':')
    userInput = input()
    fileContent = madRegex.sub(userInput, fileContent, 1)

print('\nModified Content:')
print(fileContent)
        
# writing to a file 
file = open('.\Mad Libs Files\madLibs_output.txt', 'w')
file.write(fileContent)
file.close()
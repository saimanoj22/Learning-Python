from pathlib import Path

# basic interaction with files
p = Path('spam.txt')
p.write_text('Hello, World!')   # writes text to file
p.read_text()                   # reads contents of file

# most common way
# opening file
helloFile = open(Path.home() / 'hello.txt')  # opens a file for accessing contents
# reading file
helloContent = helloFile.read()              # reads contents of file
sonnetFile = open(Path.home() / 'sonnet.txt')
# reads new lines
sonnetFile.readlines()                       # reads file contents along with new line characters and returns list with each line as element
# writing files
baconFile = open('bacon.txt', 'w')  # open file in write mode, if text already exists it gets overwritten by new text
baconFile.write('Hello, World!\n')
# closing file
baconFile.close()
baconFile = open('bacon.txt', 'a')  # open file in append mode, appends entered text to already existing text
baconFile.write('Bacon is not a vegetable.')

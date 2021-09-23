# Shutil module which has basic operations of organizing files
import shutil, os

# copying files from source to desination
shutil.copy('source', 'desination')
shutil.copytree('source', 'desination') # copies a folder along with all subfolders and directories

# movingand renaming files
shutil.move('source', 'desination')
    # if a file already exists then the file renames using same shutil.move command

# permanently deleting files and folders
os.unlink('path')       # deletes a file at the given path
os.rmdir('path')        # deletes a folder at the given path. The folder must be empty of any files and folders.
shutil.rmtree('path')   # deletes the folder at the given path along with all its contents like files and subfolders

# safe deletes with the send2trash module
import send2trash
send2trash.send2trash('path')   # do not delete files permanently instead send them to trash

# walking a directory tree (os.walk())
'''
Ex : Consider following file system

C:\
|__delicious
    |
    |__cats
    |   |__catnames.txt
    |   |__zophie.jpg
    |
    |__walnut
    |   |__waffles
    |       |__buffer.txt
    |
    |__spam.txt
'''
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

'''
os.walk() is passed a single string value (the path of the folder) and it returns three values on each iteration through the loop : 
    • a string of the current folder's name
    • a list of strings of the folders in the current folder
    • a list of strings of the files in the current folder
'''

# compressing files with zipfile module
import zipfile
from pathlib import Path

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip') # opening a zip file from home directory

# getting list of files and folders in a zipfile
exampleZip.namelist()

# getting info of a file in the zipfile
spamInfo = exampleZip.getinfo('spam.txt')   # assume we have a file named spam.txt in example.zip
# file size of above info collected file
spamInfo.file_size()
# compressing the file size
spamInfo.compress_size()
# compression factor
print(round(spamInfo.file_size / spamInfo. compress_size, 2))

# extracting all files from zip file
exampleZip.extractall()

# extracting specific (single) files
exampleZip.extract('path')              # path must match to one of the item from list in namelist() command
exampleZip.extract('path', 'secondArg') # passing second argument lets the command to extract file into the path given in second argument instead of in current directory

# closing zip file after the operations are done
exampleZip.close()

# creating and adding to zip files
'''
To create zip file we must open the file object with 'w' parameter as second argument
After we have to use write function to convert into zip file
write function has two arguments the file name and compression type parameter
here we use deflate compression algorithm which works well on all types of data
'''
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close() 
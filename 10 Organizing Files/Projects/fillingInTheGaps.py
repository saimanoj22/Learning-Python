#!python
# fills gaps in between names of files in a folder

import shutil, os, re
from pathlib import Path

def fillGaps(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        flag = 1
        max_len = 0
        for filename in filenames:
            #print(filename)

            # gets the name of the file
            fileText = Path(os.path.join(foldername, filename)).name
            fileRegex = re.compile('(\d{1,})(.\w+)')
            mo = fileRegex.search(fileText)
            #print(mo.group(1))

            # maximum length of number in filename, for padding zeros
            if max_len < len(mo.group(1)):
                max_len = len(mo.group(1))
            
            if int(mo.group(1)) != flag:
                newFile = 'spam_' + '0'*(max_len - len(str(flag))) + str(flag) + mo.group(2)
                # prints old file and new file file name
                print(os.path.join(foldername, filename))
                print(os.path.join(foldername, newFile))
                # renames files
                #shutil.move(os.path.join(foldername, filename), os.path.join(foldername, newFile))
                print("Renaming Done...")
            flag += 1

fillGaps('C:\\Users\\DELL\\OneDrive\\Desktop\\Labs\\zz text')
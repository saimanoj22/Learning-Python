# module of path 
from pathlib import Path

# os module
import os

# displays path
Path('spam','bacon','eggs')

# returns path as string (along with escape characters for backslashes)
str(Path('spam','bacon','eggs'))

# / operator for joining paths
Path('spam') / 'bacon' / 'eggs'

# also join method can used for strings
'\\'.join(['spam','bacon','egggs'])

# current working directory
Path.cwd()
os.getcwd()

# change current working directory
os.chdir("<'new directory path'>")

# the home directory
Path.home()

# create new dirs or folders
os.makedirs('C:\\delicious\\walnut\\waffles') # creats multiple subdirectories
Path(r'C:\Users\Name\spam').mkdir() # creates one folder(spam) at a time

# check absolute and relative paths 
Path.cwd().is_absolute()
os.path.abspath('path') # return a string of absolute path of argument
os.path.isabs('path')  # return bool value whether is absolute path or not
os.path.relpath('c_path, start') # returns string of relative path from start path to c_path.(if start not provided default value is cwd())

# PARTS OF FILE PATH
# i) from pathlib
'''
Ex : C:\Users\Name\spam.txt

C:              -> Drive
C:\             -> Anchor
\Users\Name\    -> Parent
spam.txt        -> Name
spam            -> Stem
.txt            -> Suffix
'''
p = Path('C:\Users\Name\spam.txt')
p.anchor    # returns anchor
p.parent    # returns parent
p.name      # returns name
p.stem      # returns stem
p.suffix    # returns suffix
p.drive     # returns drive
p.parents['arg'] # returns path of respective parent as example below
'======================================================================'
Path.cwd()
#WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
Path.cwd().parents[0]
#WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
Path.cwd().parents[1]
#WindowsPath('C:/Users/Al/AppData/Local/Programs')
Path.cwd().parents[2]
#WindowsPath('C:/Users/Al/AppData/Local')
Path.cwd().parents[3]
#WindowsPath('C:/Users/Al/AppData')
Path.cwd().parents[4]
#WindowsPath('C:/Users/Al')
Path.cwd().parents[5]
#WindowsPath('C:/Users')
Path.cwd().parents[6]
#WindowsPath('C:/')
'======================================================================'

# ii) from os
'''
Ex : C:\Windows\System32\calc.exe

C:\Windows\System32     -> Dir Name
calc.exe                -> Base Name
'''
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.dirname             # returns dir name
os.path.basename            # returns base name
os.path.split               # returns tuple with dir name  and base name
calcFilePath.split(os.sep)  # returns list of all the parts of the path as strings

# get file size and contents of folder
os.path.getsize('C:\\Windows\\System32\\calc.exe')  # returns file size in bytes
os.listdir('C:\\Windows\\System32')                 # retuns list of strings of file names in the dir

# glob patterns
p = Path('C:/Users/Name/Desktop')
p.glob('*')             # generator object
list[p.glob('*')]       # list of all files in given path
list[p.glob('*.txt')]   # this glob can be used like regex to sort specific formats of files
list[p.glob('*.?x?')]   # sort out files of format like .txt, .exe

# checking path validity
p = Path('C:\Users\Name\spam')
p.exists()  # returns bool type whether path exists
p.is_dir()  # returns bool type whether is directory 
p.is_file() # returns bool type whether is file
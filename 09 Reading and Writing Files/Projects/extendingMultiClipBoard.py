# This file is for just writing code 
# Original file is .pyw format file which is used to run code in machine
# the .pyw file is in "Extending Multi Clipboard" folder in Projects section

#! python
# exmcb.pyw - Saves, delete and loads pieces of text to the clipboard.
# Usage: py.exe exmcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe exmcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe exmcb.pyw list - Loads all keywords to clipboard.
#        py.exe exmcb.pyw delete <keyword> - Deletes the specific keyword.
#        py.exe exmcb.pyw delete - Deletes all keywords.

import shelve, pyperclip, sys

exmcbShelf = shelve.open('exmcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        exmcbShelf[sys.argv[2]] = pyperclip.paste()
# Added delete option for deleting keywords
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del exmcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
     # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(exmcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for keyword in exmcbShelf:
            del exmcbShelf[keyword]
    elif sys.argv[1] in exmcbShelf:
        pyperclip.copy(exmcbShelf[sys.argv[1]])

exmcbShelf.close()
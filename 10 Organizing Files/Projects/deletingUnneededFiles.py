#!python
# Deletes all files of size more than 100MB  

import shutil, os, send2trash
from pathlib import Path

def delete100MB(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filePath = os.path.join(foldername, filename)
            if os.path.getsize(filePath) > 104857600:
                # prints the path of file being deleted
                print(filePath)
                # for safe deletion -> sent to recyclebin
                send2trash.send2trash(filePath)
                # for permanent deletion
                #os.unlink(filePath)

delete100MB('C:\\Users\\DELL\\OneDrive\\Desktop\\Labs\\zz text')
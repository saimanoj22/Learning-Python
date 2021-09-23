#!python
# Copies desired formats of files from specified folder

import shutil, os
from pathlib import Path

def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    desination = 'new path'
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            #print(foldername, filename)
            #print((Path(filename).suffix).lower())
            if (Path(filename).suffix).lower() in ('.pdf','.jpg'):
                filePath = os.path.join(folder,filename)
                #print(filePath)
                #print(foldername, filename)
                #open(os.path.join(foldername, filename))
                #print(folder,desination)
                shutil.copy(filePath, desination)

selectiveCopy('current path of folder to be copied')
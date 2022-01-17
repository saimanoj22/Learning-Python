# This program checks all words from a text file to decrpyt a PDF file.

import PyPDF2
PDFfile = open('encryptedminuted.pdf', 'rb')
PDFReader = PyPDF2.PdfFileReader(PDFfile)

file = open('dictionary.txt')
fileContent = file.read()
fileContent = fileContent.split('\n')

flag = ''
for password in fileContent:
    if PDFReader.decrypt(password.lower()) ==  1:
        flag = password.lower()
        break
    elif  PDFReader.decrypt(password.upper()) == 1:
        flag = password.upper()
        break
    else:
        continue
print('Password Found.....')
print('PASSWORD :',flag)

from logging import root
from tkinter import filedialog
from PyPDF2 import PdfReader
import os

os.system('cls')

root.directory = filedialog.askdirectory()

route = root.directory+'/'

archivos = os.listdir(route)


for archivo in archivos:
    pdfFileObject   = open(route+archivo,'rb')
    pdfReader       = PdfReader(pdfFileObject)
    pageObject      = pdfReader.pages[0]
    text            = pageObject.extract_text()
    textLength      = len(text)
    accountNumber   = ""

    for letter in range(textLength):
        if text[letter]=="E" and text[letter+1]=="s" and text[letter+2]=="t" and text[letter+3]=="u" and text[letter+4]=="d" and text[letter+5]=="i" and text[letter+6]=="a" and text[letter+7]=="n" and text[letter+8]=="t" and text[letter+9]=="e" and text[letter+10]==":":
            accountNumber = text[letter+11:text.find("Usuario")]
            accountNumber = accountNumber.strip()
            pdfFileObject.close()

            os.renames(route+archivo,route+accountNumber+'.pdf')
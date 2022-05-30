import os, re

filepath = 'C:\\Users\\santi\\PycharmProjects\\pythonProject\\Computacion\\TP 2\\SecretKey'
numero = r'\d'
filenames = os.listdir(filepath)

for name in filenames:
    newname = re.sub(numero, '', name)
    os.rename(filepath + '\\' + name, filepath + '\\' + newname)

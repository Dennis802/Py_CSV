import csv
import sys
import re
import os


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    running_mode = 'Frozen/executable'
else:
    try:
        app_full_path = os.path.realpath(__file__)
        application_path = os.path.dirname(app_full_path)
        running_mode = "Non-interactive (e.g. 'python myapp.py')"
    except NameError:
        application_path = os.getcwd()
        running_mode = 'Interactive'

def getPath(varname):
    config_full_path = os.path.join(application_path, varname)
    return config_full_path


brands = getPath('merken.txt')
prodtype = getPath('types.txt')
brandings = getPath('brandings.txt')
kleuren = getPath('kleuren.txt')


def readTextFile(filename):
    my_file = open(filename, "r")
    rawdata = my_file.read()
    datalist = rawdata.split("\n")
    return datalist


def getStringPart(filename):
    for i in readTextFile(filename):
        r1 = re.findall(i, searchResult)
        if r1:
            stringpart = ' '.join(r1)
            if stringpart != '':
                return stringpart
            else:
                pass


def searchCSV(filename, itemnumber):
    csv_file = csv.reader(open(filename, "r", encoding='utf-8'), delimiter=",")
    for row in csv_file:
        if itemnumber == row[0]:
            return row
        elif itemnumber == row[1]:
            return row
        elif itemnumber == row[2]:
            return row


string = input("Input pls: ")

searchResult = searchCSV(getPath('EAN.csv'), string)[2]
EAN = searchCSV(getPath('EAN.csv'), string)[::-1][2]

model = re.search(f'{getStringPart(brands)}(.*){getStringPart(prodtype)}', str(searchResult)).group(1)

try:
    cc = searchCSV('kleurcodes.csv', getStringPart(kleuren))
    colorcode, rval, gval, bval = cc[1], cc[2], cc[3], cc[4]
except:
    pass

print('\n' + searchResult, '\n')
print("Artikelnummer:", string)
print("Merk:", getStringPart(brands))
print("Modelnaam:", model[1:])
print("Productsoort:", getStringPart(prodtype))
try:
    print("Kleur:", getStringPart(kleuren))
except:
    pass
print("Branding:", getStringPart(brandings))
print("EAN13:", EAN)
try:
    print(f'{colorcode}, R:{rval}, G:{gval}, B:{bval}')
except:
    pass
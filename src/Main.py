from ArrayOfPoint import *
from Matrix import *

file = open("test1.txt", "r")
size = int(file.readline().split("\n"))
file.readline() # skip blank

pointRead = False
arrayPoint = ArrayOfPoint()

while (not pointRead):
    temp = file.readline()
    if temp[0] == '\n': #mengecek jika semua point pada file sudah dibaca
        pointRead = True
    else: #mulai pembacaan point
        name = ""
        x = "" # masih dalam bentuk string
        y = "" # masih dalam bentuk string
        section = 0
        for i in temp:
            if (i != ' ' and section == 0):
                # section 0 = section untuk membaca nama dari point
                name = name + i
            elif (i != ' ' and section == 1):
                # section 1 = section untuk membaca koordinat x dari point
                x = x + i
            elif (i != ' ' and i != '\n' and section == 2):
                # section 2 = section untuk membaca koordinat y dari point
                y = y + i
            else :
                section += 1
        arrayPoint.AddPoint(name, int(x),int(y)) # point ditambahkan kedalam array

print(size)
print()
arrayPoint.PrintArray()
file.close()
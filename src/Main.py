# import networkx as nx
# import matplotlib.pyplot as plt
from ArrayOfPoint import *
from Matrix import *
from Graph import *

file = open("test/test3.txt", "r")

# MEMBACA BANYAK POINT PADA GRAF
size = int(file.readline().split("\n")[0])
file.readline() # skip blank

# MEMBACA DAN MENYIMPAN POINT KEDALAM ARRAY
pointRead = False # penanda apakah semua point telah dibaca
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
        arrayPoint.AddPoint(name, float(x), float(y)) # point ditambahkan kedalam array

# MEMBACA MATRIKS KETETANGGAAN
matrix = Matrix(size+1)
matrixRead = False
itr = 0

while (itr < size+1):
    temp = ""
    for i in file.readline():
        if (i != ' ' and i != '\n'):
            temp = temp + i
        else:
            matrix.AddElementToMatrix(temp)
            temp = ""
    itr += 1
file.close()

# MAIN PROGRAM
print("Daftar Point:")
arrayPoint.PrintDaftarNamaPoint()
simpulAwal = input(str("Masukkan simpul awal: "))
simpulTujuan = input(str("Masukkan simpul tujuan: "))
print(f"Jalur Terpendek = {arrayPoint.PathWithAStar(simpulAwal, simpulTujuan, matrix)}")
print(f"Jarak tempuh = {arrayPoint.DistanceWithAStar(simpulAwal, simpulTujuan, matrix)}")
print("Otewe tampilin graf...")
printGraph(arrayPoint, arrayPoint.PathWithAStar(simpulAwal, simpulTujuan, matrix), matrix)

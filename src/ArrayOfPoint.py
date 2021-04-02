from Point import *

class ArrayOfPoint :
    def __init__ (self):
        self.mem = []
        self.size = 0

    def FindPoint(self, name):
        # fungsi untuk mencari point pada array dan mereturn point tersebut
        # jika tidak ditemukan, fungsi mereturn None.
        for point in self.mem:
            if point.name == name:
                return point
        return None

    def AddPoint(self, name, x, y):
        # fungsi untuk menambahkan sebuah point kedalam array. 
        # jika berhasil ditambahkan, fungsi mereturn True.
        # jika gagal ditambahkan (karena point dgn nama yg sama sudah ada), fungsi mereturn False.
        if self.FindPoint(name) == None:
            newPoint = Point(name, x, y)
            self.mem.append(newPoint)
            self.size += 1
            return True
        return False
    
    def RemovePoint(self, name):
        # fungsi untuk menghapus sebuah point dari array. 
        # jika berhasil dihapus, fungsi mereturn True.
        # jika gagal dihapus (karena point dgn nama tersebut memang tidak ada), fungsi mereturn False.
        for i in range(self.size):
            if self.mem[i].name == name:
                self.mem.pop(i)
                return True
        return False

    def PrintArray(self):
        # prosedur untuk mencetak isi array ke layar.
        # prosedur ini hanya digunakan untuk testing.
        for point in self.mem:
            print(f"{point.name}({point.x}, {point.y})")
from Point import *
from PrioQueue import *
from Matrix import * 

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
            print(f"{point.name} ({point.x},{point.y})")
    
    def EuclidianDistance(self, startName, endName):
        # fungsi akan mereturn jarak antara 2 titik jika ditarik garis lurus
        start = self.FindPoint(startName)
        end = self.FindPoint(endName)
        return math.sqrt((start.x - end.x)**2 + (start.y - end.y)**2)
    
    def GetListOfAdjacentPointName(self, pointName, matrix):
        i = 0
        ListOfAdjacentPointName = []
        while i < matrix.matrix_size:
            # mencari kolom dengan nama point yang sama
            if (pointName == matrix.matrix_adj[0][i]):
                j = 0
                # membaca isi dari kolom
                for j in range(matrix.matrix_size):
                    if (matrix.matrix_adj[j][i] == "1"):
                        ListOfAdjacentPointName.append(matrix.matrix_adj[j][0])
                return ListOfAdjacentPointName
            else:
                i += 1
        return ListOfAdjacentPointName


    def DistanceWithAStar(self, startName, endName, matrix):
        simpulHidup = PrioQueue()
        simpulHidup.AddElmt(startName, 0, self.EuclidianDistance(startName, endName), startName)
        visitedList = [startName]
        currentPointName = startName

        if (startName == endName):
            return -1 # error : simpul tujuan tidak dapat didatangi dari simpul asal
        while (currentPointName != endName):
            
            # memasukkan semua tetangga dari point sekarang yang belum pernah dikunjungi kedalam simpulHidup
            adjacentPointName = self.GetListOfAdjacentPointName(currentPointName, matrix)
            for pointName in adjacentPointName:
                # mengecek apakah point sudah pernah dikunjungi
                visited = False
                for visitedPoint in visitedList:
                    if (visitedPoint == pointName):
                        visited = True
                if (not visited):
                    visitedList.append(pointName)
                    # g(n) = g(n) + jarak titik sekarang ke titik tetangga ini
                    traveledDistance = simpulHidup.mem[0].traveledDistance + self.EuclidianDistance(currentPointName, pointName)
                    # f(n) = g(n) + jarak euclidian titik tetangga ini ke titik tujuan
                    estimatedDistance = traveledDistance + self.EuclidianDistance(pointName, endName)
                    traveledPath = simpulHidup.mem[0].traveledPath + " > " + pointName
                    simpulHidup.AddElmt(pointName, traveledDistance, estimatedDistance, traveledPath)

            # menghapus titik sekarang dari simpul hidup karena sudah selesai dikunjungi
            simpulHidup.RemoveHead()

            # mengecek apakah simpulHidup sudah kosong
            if (simpulHidup.size == 0):
                return -1 # error : simpul tujuan tidak dapat didatangi dari simpul asal
            else:
                currentPointName = simpulHidup.mem[0].name
            
        # simpul hidup ditemukan
        return simpulHidup.mem[0].traveledDistance

    def PathWithAStar(self, startName, endName, matrix):
        simpulHidup = PrioQueue()
        simpulHidup.AddElmt(startName, 0, self.EuclidianDistance(startName, endName), startName)
        visitedList = [startName]
        currentPointName = startName

        if (startName == endName):
            return "unreachable" # error : simpul tujuan tidak dapat didatangi dari simpul asal
        while (currentPointName != endName):
            
            # memasukkan semua tetangga dari point sekarang yang belum pernah dikunjungi kedalam simpulHidup
            adjacentPointName = self.GetListOfAdjacentPointName(currentPointName, matrix)
            for pointName in adjacentPointName:
                # mengecek apakah point sudah pernah dikunjungi
                visited = False
                for visitedPoint in visitedList:
                    if (visitedPoint == pointName):
                        visited = True
                if (not visited):
                    visitedList.append(pointName)
                    # g(n) = g(n) + jarak titik sekarang ke titik tetangga ini
                    traveledDistance = simpulHidup.mem[0].traveledDistance + self.EuclidianDistance(currentPointName, pointName)
                    # f(n) = g(n) + jarak euclidian titik tetangga ini ke titik tujuan
                    estimatedDistance = traveledDistance + self.EuclidianDistance(pointName, endName)
                    traveledPath = simpulHidup.mem[0].traveledPath + " > " + pointName
                    simpulHidup.AddElmt(pointName, traveledDistance, estimatedDistance, traveledPath)

            # menghapus titik sekarang dari simpul hidup karena sudah selesai dikunjungi
            simpulHidup.RemoveHead()

            # mengecek apakah simpulHidup sudah kosong
            if (simpulHidup.size == 0):
                return "unreachable" # error : simpul tujuan tidak dapat didatangi dari simpul asal
            else:
                currentPointName = simpulHidup.mem[0].name
            
        # simpul hidup ditemukan
        return simpulHidup.mem[0].traveledPath

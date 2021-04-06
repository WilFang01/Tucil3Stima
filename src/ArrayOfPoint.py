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
        # fungsi untuk mendapatkan titik tetangga dari titik yang diinput
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
        # fungsi untuk mendapatkan jarak terpendek menggunakan metode astar

        simpulHidup = PrioQueue()
        # memasukkan simpul awal kedalam simpul hidup sebagai titik yang akan diproses pertama
        simpulHidup.AddElmt(startName, 0, self.EuclidianDistance(startName, endName), startName)
        visitedList = []
        currentPointName = startName

        if (startName == endName):
            return 0 # jarak 0 karena titik asal dan tujuan sama
        while (currentPointName != endName):
            # Tandai titik sekarang sudah pernah dikunjungi
            visitedList.append(currentPointName)
            adjacentPointName = self.GetListOfAdjacentPointName(currentPointName, matrix)

            # memasukkan semua tetangga dari point sekarang yang belum pernah dikunjungi kedalam simpulHidup
            for pointName in adjacentPointName:
                # mengecek apakah point sudah pernah dikunjungi
                visited = False
                for visitedPoint in visitedList:
                    if (visitedPoint == pointName):
                        visited = True
                if (visited == False):
                    # g(n) = g(n) + jarak titik sekarang ke titik tetangga ini
                    traveledDistance = simpulHidup.mem[0].traveledDistance + self.EuclidianDistance(currentPointName, pointName)
                    # f(n) = g(n) + jarak euclidian titik tetangga ini ke titik tujuan
                    estimatedDistance = traveledDistance + self.EuclidianDistance(pointName, endName)
                    traveledPath = simpulHidup.mem[0].traveledPath + " > " + pointName
                    # dimasukkan kedalam simpul hidup
                    simpulHidup.AddOrExchageElmt(pointName, traveledDistance, estimatedDistance, traveledPath)

            # menghapus titik sekarang dari simpul hidup karena sudah selesai dikunjungi
            simpulHidup.RemoveHead()

            # mengecek apakah simpulHidup sudah kosong, jika kosong pencarian rute dihentikan.
            if (simpulHidup.size == 0):
                return -1 # error : simpul tujuan tidak dapat didatangi dari simpul asal
            # jika belum kosong, lanjut ke titik selanjutnya
            else:
                currentPointName = simpulHidup.mem[0].name
            
        # simpul tujuan ditemukan
        return simpulHidup.mem[0].traveledDistance

    def PathWithAStar(self, startName, endName, matrix):
        # fungsi untuk mendapatkan jalur terpendek menggunakan metode astar
        simpulHidup = PrioQueue()
        # memasukkan simpul awal kedalam simpul hidup sebagai titik yang akan diproses pertama
        simpulHidup.AddElmt(startName, 0, self.EuclidianDistance(startName, endName), startName)
        visitedList = []
        currentPointName = startName

        if (startName == endName):
            return "You have arrived at your destination" # sudah sampai karena titik asal dan tujuan sama
        while (currentPointName != endName):
            # Tandai titik sekarang sudah pernah dikunjungi
            visitedList.append(currentPointName)
            adjacentPointName = self.GetListOfAdjacentPointName(currentPointName, matrix)

            # memasukkan semua tetangga dari point sekarang yang belum pernah dikunjungi kedalam simpulHidup
            for pointName in adjacentPointName:
                # mengecek apakah point sudah pernah dikunjungi
                visited = False
                for visitedPoint in visitedList:
                    if (visitedPoint == pointName):
                        visited = True
                if (visited == False):
                    # g(n) = g(n) + jarak titik sekarang ke titik tetangga ini
                    traveledDistance = simpulHidup.mem[0].traveledDistance + self.EuclidianDistance(currentPointName, pointName)
                    # f(n) = g(n) + jarak euclidian titik tetangga ini ke titik tujuan
                    estimatedDistance = traveledDistance + self.EuclidianDistance(pointName, endName)
                    traveledPath = simpulHidup.mem[0].traveledPath + " > " + pointName
                    # dimasukkan kedalam simpul hidup
                    simpulHidup.AddOrExchageElmt(pointName, traveledDistance, estimatedDistance, traveledPath)

            # menghapus titik sekarang dari simpul hidup karena sudah selesai dikunjungi
            simpulHidup.RemoveHead()

            # mengecek apakah simpulHidup sudah kosong, jika kosong pencarian rute dihentikan.
            if (simpulHidup.size == 0):
                return "unreachable" # error : simpul tujuan tidak dapat didatangi dari simpul asal
            # jika belum kosong, lanjut ke titik selanjutnya
            else:
                currentPointName = simpulHidup.mem[0].name
            
        # simpul tujuan ditemukan
        return simpulHidup.mem[0].traveledPath

    def GetMinPoint(self):
        # fungsi untuk mendapatkan point terkecil.
        # point terkecil tersusun oleh nilai x terkecil pada semua titik dan nilai y terkecil pada semua titik 
        minPoint = Point("min", self.mem[0].x, self.mem[0].y)
        for point in self.mem:
            if (point.x < minPoint.x):
                minPoint = Point("min", point.x, minPoint.y)
            if (point.y < minPoint.y):
                minPoint = Point("min", minPoint.x, point.y)
        return minPoint

    def GetMaxPoint(self):
        # fungsi untuk mendapatkan point terkecil.
        # point terkecil tersusun oleh nilai x terbesar pada semua titik dan nilai y terbesar pada semua titik 
        maxPoint = Point("max",self.mem[0].x, self.mem[0].y)
        for point in self.mem :
            if (point.x > maxPoint.x):
                maxPoint = Point("max",point.x, maxPoint.y)
            if (point.y > maxPoint.y):
                maxPoint = Point("max",maxPoint.x, point.y)
        return maxPoint

    def PrintDaftarNamaPoint(self):
        # prosedur untuk menampilkan semua nama titik yang telah diinput ke layar
        print("Daftar Nama Point :")
        for point in self.mem:
            print(f"- {point.name}")

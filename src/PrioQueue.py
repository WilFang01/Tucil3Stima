class ElmtPrioQueue :
    def __init__(self, name, traveledDistance, estimatedDistance, traveledPath):
        self.name = name # nama titik ini
        self.traveledDistance = traveledDistance # nilai g(n)
        self.estimatedDistance = estimatedDistance # nilai f(n) = g(n) + h(n), dgn h(n) jarak euclidian ke titik tujuan
        self.traveledPath = traveledPath # untuk menyimpan jalan yang dilalui dari titik awal ke tujuan

class PrioQueue :
    def __init__(self):
        self.mem = []
        self.size = 0
    
    def AddElmt(self, name, traveledDistance, estimatedDistance, traveledPath):
        # prosedur untuk menambahkan elemen baru kedalam queue
        # jika kondisi awal kosong atau hanya ada 1 elemen maka proses menambahkan elemen normal seperti queue biasa.
        # jika kondisi awal terdapat lebih dari 1 elemen, maka elemen disisipkan berdasarkan nilai estimatedDistance.
        # nilai estimatedDistance terkecil akan berada pada head dari queue.
        # pensisipan elemen baru dimulai dari elemen kedua 
        # (elemen paling depan tidak boleh digeser sama sekali, bahkan saat nilai estimatedDistancenya lebih besar)
        Elmt = ElmtPrioQueue(name, traveledDistance, estimatedDistance, traveledPath)
        if self.size == 0 or self.size == 1:
            self.mem.append(Elmt)
            self.size += 1
        else:
            i = 1
            while (i < self.size):
                if (self.mem[i].estimatedDistance > estimatedDistance):
                    self.mem.insert(i, Elmt)
                    self.size += 1
                    break
                i += 1
            if i == self.size:
                self.mem.append(Elmt)
                self.size += 1
    
    def RemoveHead(self):
        # prosedur untuk menghapus elemen pertama prioqueue
        self.mem.pop(0)
        self.size -= 1

    def FindElmt(self, name):
        # fungsi untuk mencari elemen dengan nama sesuai input
        for elmt in self.mem:
            if elmt.name == name:
                return elmt
        return None

    def AddOrExchageElmt(self, pointName, traveledDistance, estimatedDistance, traveledPath):
        # prosedur untuk menambahkan sebuah elemen kedalam prioqueue
        # jika elemen titik yang ingin ditambahkan ternyata sudah pernah ada sebelumnya,
        # akan dibandingkan terlebih dahulu.
        # jika estimatedDistancenya elemen baru lebih kecil dari yang ada di queue, 
        # maka elemen lama akan dihapus dan elemen baru dimasukkan.
        idx = 0
        for i in range(self.size):
            if self.mem[i].name == pointName:
                if self.mem[i].estimatedDistance > estimatedDistance:
                    idx = i
        if idx != 0:
            self.mem.pop(idx)
        self.AddElmt(pointName, traveledDistance, estimatedDistance, traveledPath)
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
        self.mem.pop(0)
        self.size -= 1

    def FindElmt(self, name):
        for elmt in self.mem:
            if elmt.name == name:
                return elmt
        return None

    def ExchageElmt(self, pointName, traveledDistance, estimatedDistance, traveledPath):
        idx = 0
        for i in range(self.size):
            if self.mem[i].name == pointName:
                idx = i
        if idx != 0:
            self.mem.pop(idx)
        self.AddElmt(pointName, traveledDistance, estimatedDistance, traveledPath)
import math

class Point :
    # Setup
    def __init__ (self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

    def JarakEuclidianKe(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
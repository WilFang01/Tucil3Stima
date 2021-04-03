class Matrix :
    # Setup
    def __init__(self, size):
        self.matrix_adj = [[999 for i in range(size)] for i in range(size)]
        self.matrix_size = size

    def AddElementToMatrix(self, elmt):
        # fungsi untuk menambahkan element pada matriks
        # jika berhasil ditambahkan, fungsi mereturn true
        # jika gagal, fungsi mereturn false
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.matrix_adj[i][j] == 999:
                    self.matrix_adj[i][j] = elmt
                    return True
        return False
    
    def GetElement(self, i, j):
        return self.matrix_adj[i+1][j+1]
    
    def PrintMatrix(self):
        # prosedur untuk mencetak isi matriks ke layar
        for row in range(self.matrix_size):
            for col in range(self.matrix_size):
                print(self.matrix_adj[row][col], end=" ")
            print()
    
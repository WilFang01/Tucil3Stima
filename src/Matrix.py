class Matrix :
    # Setup
    def __init__(self, size):
        self.matrix_adj = [[999 for i in range(size)] for i in range(size)]
        self.matrix_size = size

    def AddElementToMatrix(self, number):
        # fungsi untuk menambahkan element pada matriks
        # jika berhasil ditambahkan, fungsi mereturn true
        # jika gagal, fungsi mereturn false
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix_adj[i][j] == 999:
                    self.matrix_adj[i][j] = number
                    return True
        return False
    
    
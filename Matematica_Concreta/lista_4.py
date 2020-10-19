class Matrix(object):
   def __init__(self):
        self.matrix = []
        self.mat_size = input("Insira o tamanho da matriz quadrada: ")
        
        try:
            self.mat_size = int(self.mat_size)
        except ValueError:
            raise Exception("Apenas valores inteiros sao permitidos.")
        
        for i in range(self.mat_size):
            self.matrix.append([])
            
        
        for i in range(self.mat_size):
            for j in range(self.mat_size):
                print("Insira o valor da matriz na linha", i, "e coluna", j,".")
                value = input()
                try:
                    value = float(value)
                except ValueError:
                    raise Exception("Apenas valores numericos sao permitidos.")
                self.matrix[i].append(value) 


class First_Question(Matrix):

    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if j > i:
                    valor += self.matrix[i][j]
        
        print(valor)


class Second_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if (j + i) < (self.mat_size-1):
                    valor += self.matrix[i][j]
        
        print(valor)
        


class Third_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if ((j + i) < (self.mat_size-1)) and j>i:
                    valor += self.matrix[i][j]
        
        print(valor)


class Fourth_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if j>i and ((j + i) > (self.mat_size-1)):
                    valor += self.matrix[i][j]
        
        print(valor)


class Fifth_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i>j:
                    valor += self.matrix[i][j]
        
        print(valor)


class Sixth_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i>j and ((j + i) > (self.mat_size-1)):
                    valor += self.matrix[i][j]
        
        print(valor)


class Seventh_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i>j and ((j + i) < (self.mat_size-1)):
                    valor += self.matrix[i][j]
        
        print(valor)


class Eighth_Question(Matrix):
    def __init__(self):
        
        super().__init__()
        
        valor = 0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if ((j + i) > (self.mat_size-1)):
                    valor += self.matrix[i][j]
        
        print(valor)



#First_Question()
#Second_Question()
#Third_Question()
#Fourth_Question()
#Fifth_Question()
#Sixth_Question()
#Seventh_Question()
Eighth_Question()













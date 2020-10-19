class Sixth_Question:
    def __init__(self):
        self.value = 0
        self.x = []
        self.y = []
        
        print("Selecione os valores que deseja adicionar na sequencia X, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
        
            self.x.append(numerical_value)

        print("Selecione os valores que deseja adicionar na sequencia Y, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
        
            self.y.append(numerical_value)


        self.n = input("Insira o limite superior do somatorio:")

        
        try:
            self.n = int(self.n)
            
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.n < 1:
            raise Exception("Apenas valores acima de 0 sao permitidos.")
        
        if (self.n > len(self.x)) or (self.n > len(self.y)):
            raise Exception("O valor de n deve ser menor que o comprimento da sequencia X e Y.")
    
    
    def calculate(self):
        self.value = self.x[0] * self.y[0]
        if self.n > 1:
            for i in range (1, self.n):
                self.value += (self.x[i] * self.y[i])
        
        
        print(self.value)


class Seventh_Question:
    def __init__(self):
        self.value = 0
        self.n = input("Insira o valor do limite superior:")
        
        try:
            self.n = int(self.n)
            
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
            
        if self.n < 1:
            raise Exception("Apenas valores acima de 0 sao permitidos.")
        
        
    def calculate(self):
        print((self.n*(self.n + 1))/2)

class Eighth_Question:
    def __init__(self):
        self.x = []
        
        
        print("Selecione os valores que deseja adicionar na sequencia X, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
        
            self.x.append(numerical_value)
    
        self.n = input("Insira o valor do limite superior:")
        
        try:
            self.n = int(self.n)
            
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.n < 1:
            raise Exception("Apenas valores acima de 0 sao permitidos.")
        
        if self.n > len(self.x):
            raise Exception("O valor de n deve ser menor que o comprimento da sequencia X.")
    
    def calculate(self):
        
        self.value = self.x[0]**2
        if self.n > 1:
            for i in range (1, self.n):
                self.value += (self.x[i]**2)
        
        print(self.value)


class Nineth_Question:
    def __init__(self):
        self.value = 0
        self.n = input("Insira o valor do limite superior:")
        
        try:
            self.n = int(self.n)
            
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.n < 0:
            raise Exception("Apenas valores nao negativos sao permitidos.")
        
        
    def calculate(self):
        print(2**(self.n+1)-1)        


class Tenth_Question:
    def __init__(self):
        self.value = 0
        self.x = []
        self.y = []
        
        print("Selecione os valores que deseja adicionar na sequencia X, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
        
            self.x.append(numerical_value)

        print("Selecione os valores que deseja adicionar na sequencia Y, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
        
            self.y.append(numerical_value)


        self.n = input("Insira o limite superior do somatorio:")

        
        try:
            self.n = int(self.n)
            
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.n < 1:
            raise Exception("Apenas valores acima de 0 sao permitidos.")
        
        if (self.n > len(self.x)) or (self.n > len(self.y)):
            raise Exception("O valor de n deve ser menor que o comprimento da sequencia X e Y.")
    
    
    def calculate(self):
        self.value = (1/self.x[0])+(1/self.y[0])
        if self.n > 1:
            for i in range (1, self.n):
                self.value += ((1/self.x[i])+(1/self.y[i]))
        
        
        print(self.value)

#Sixth_Question().calculate()
#Seventh_Question().calculate()
#Eight_Question().calculate()
#Nineth_Question().calculate()
Tenth_Question().calculate()







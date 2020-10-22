class First_Question:
    
    def __init__(self):
        self.seq = []
        
        
        
        print("Selecione os valores que deseja adicionar na sequencia, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = int(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos inteiros sao permitidos.")
                else:
                    break
                
            
            self.seq.append(numerical_value)
        
        
    
    def calculate(self):
        subseq = []
        
        for i in range(len(self.seq)):
            if (self.seq[i] % 2) != 0:
                subseq.append(self.seq[i])
    
    
        print(subseq)
        


class Second_Question:
    
    def __init__(self):
        self.seq = []
        
        
        
        print("Selecione os valores que deseja adicionar na sequencia, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = int(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos inteiros sao permitidos.")
                else:
                    break
                
            
            self.seq.append(numerical_value)
        
        
    
    def calculate(self):
        flag = 0
        subseq = []
        
        for i in range(len(self.seq)):
            flag = 0
            if (self.seq[i] % 2) == 0:
                flag = 1
            for j in range(3,self.seq[i],2):
                if (self.seq[i] % j) == 0 or (self.seq[i]%2)==0:
                    flag = 1
            
            if flag == 0:
                subseq.append(self.seq[i])
    
        print(subseq)

        

class Third_Question:
    
    def __init__(self):
        self.seq = []
        self.seq_1 = []
        
        
        print("Selecione os valores que deseja adicionar na sequencia A, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = int(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos inteiros sao permitidos.")
                else:
                    break
                
            
            self.seq.append(numerical_value)
        
  
        print("Selecione os valores que deseja adicionar na sequencia B, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = int(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos inteiros sao permitidos.")
                else:
                    break
                
            
            self.seq_1.append(numerical_value)
            
    
    def calculate(self):
        print(self.seq_1+self.seq)


class Fourth_Question:
    
    def __init__(self):
        self.seq = []
        
        
        print("Selecione os valores que deseja adicionar na sequencia, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = int(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos inteiros sao permitidos.")
                else:
                    break
                
            
            self.seq.append(numerical_value)
        
        
        print("A contagem dos indices comeca a partir do 1")
        self.ind_a = input("Insira o indice inicial:")
        self.ind_b = input("Insira o indice final:")
        
        
        try:
            self.ind_a = int(self.ind_a)
            self.ind_b = int(self.ind_b)
        
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.ind_a > self.ind_b:
            raise Exception("O indice A deve ser menor ou igual a B.")
        
    
    def calculate(self):
        print(self.seq[self.ind_a-1:self.ind_b])


class Fifth_Question:
    def __init__(self):
        self.seq = []
        
        print("Selecione os valores que deseja adicionar na sequencia, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
                
            
            self.seq.append(numerical_value)
            
        
        self.pref = input("Escolha o comprimento do prefixo:")
        
        try:
            self.pref = int(self.pref)
        
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.pref > len(self.seq):
            raise Exception("O comprimento deve ser menor do que o tamanho da sequencia em questao.")
        
    
    
    def calculate(self):
        print(self.seq[0:self.pref])



class Sixth_Question:
    def __init__(self):
        self.seq = []
        
        print("Selecione os valores que deseja adicionar na sequencia, quando concluir pressione Enter.")
        
        
        while 1:
            numerical_value = input()
                 
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numericos sao permitidos.")
                else:
                    break
                
            
            self.seq.append(numerical_value)
            
        
        self.suf = input("Escolha o comprimento do prefixo:")
        
        try:
            self.suf = int(self.suf)
        
        except ValueError:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.suf > len(self.seq):
            raise Exception("O comprimento deve ser menor do que o tamanho da sequencia em questao.")
        
    
    
    def calculate(self):
        print(self.seq[(len(self.seq) - self.suf):])


class Menu:
    def __init__(self):
        
        questoes = ["Primeira", "Segunda", "Terceira", "Quarta", "Quinta", "Sexta"]
        
        dict_questoes = {"Primeira": First_Question, "Segunda":Second_Question, "Terceira":Third_Question,
                         "Quarta":Fourth_Question, "Quinta":Fifth_Question, "Sexta":Sixth_Question}
        
        for i in range(len(questoes)):
            print(questoes[i] + " Questao - " + str(i))
        
        self.select = input("Selecione a questão:")
        
        
        try:
            self.select = int(self.select)
        
        except:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.select > 5:
            raise Exception("Valor fora dos mencionados.")
        
        
        

        dict_questoes[questoes[self.select]]().calculate()




Menu()




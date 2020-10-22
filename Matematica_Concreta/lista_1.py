
class First_Question:
    
    def __init__(self):
        self.select = input("Selecione a letra A, B ou C: ")
        
        if self.select == "A":
            First_Question.A_Question()

        elif self.select == "B":
            First_Question.B_Question()
            
        elif self.select == "C":
            First_Question.C_Question()
            
        else:
            raise Exception("Valor fora dos mencionados.")
    
    

    def A_Question():
    
        a_array = [5]
        
        for i in range(5):
            a_array.append(a_array[-1]+3)
        
        print(a_array)
        
    
    def B_Question():
    
        a_array = [2]
        
        for i in range(5):
            a_array.append(a_array[-1]**2)
        
        print(a_array)
        
    
    def C_Question():
    
        a_array = [0]
        
        for i in range(1,6):
            a_array.append((a_array[-1]*2) +i)
        
        print(a_array)




class Second_Question:
    def __init__(self):
        
        
        
        self.PA = []
        
        print("Selecione os valores que deseja adicionar na array, quando concluir pressione Enter.")
        
        
        
        while 1:
            numerical_value = input()
            count_numerical_value = numerical_value.count("/")
            
            
            if count_numerical_value == 1 and not (any(x.isalpha() for x in numerical_value)):
                slash_position = numerical_value.find("/")
                numerical_value = float(numerical_value[0:slash_position])/float(numerical_value[slash_position+1:])
            
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numéricos são permitidos")
                else:
                    break
                
                
            self.PA.append(numerical_value)
        
        if len(self.PA) == 0:
            raise Exception("Sem valores existentes na array.")

        if len(self.PA) > 0 and len(self.PA) < 3:
            raise Exception("Valores insuficientes na array.")

                
            
    def Calculate(self):
        flag_value = round(self.PA[1] - self.PA[0], 4)
        
        
        for i in range(2, len(self.PA)):
            if (round(self.PA[i] - self.PA[i-1], 4)) == flag_value:
                continue
            else:
                raise Exception("Não é uma P.A.")

        
        
        if flag_value > 0:
            print("É uma P.A crescente.")
        if flag_value < 0:
            print("É uma P.A decrescente.")
        if flag_value == 0:
            print("É uma P.A constante.")




     

class Fifth_Question:
    def __init__(self):
        self.value1 = self.stringValidation("Insira o valor inicial da P.A:")
        self.value2 = self.stringValidation("Insira o valor final da P.A:")
        self.K = self.stringValidation("Insira a razão da P.A:")
        
        try:
            self.value1 = float(self.value1)
            self.value2 = float(self.value2)
            self.K = float(self.K)
        except ValueError:
            raise Exception("Apenas valores numéricos são permitidos")
        

        if self.value1 > self.value2 and self.K > 0:
            raise Exception("Valor da razão inválido.")
        if self.value1 < self.value2 and self.K < 0:
            raise Exception("Valor da razão inválido.")
        
        if self.K == 0:
            raise Exception("Valor da razão inválido.")
        
        if self.value1 > self.value2:
            self.flag = 1 #Crescente

        if self.value1 < self.value2:
            self.flag = 0 #Decrescente    
    
    
    def Calculate(self):
        i = 0
        array = [self.value1]
        
        if self.flag == 1:
            while array[i]+self.K > self.value2:
                array.append(array[i]+self.K)
                i+=1
        
        else:
            while array[i]+self.K < self.value2:
                array.append(array[i]+self.K)
                i+=1      
        
        array.append(self.value2)
        print(array)


    def stringValidation(self, text):
        numerical_value = input(text)
        count_numerical_value = numerical_value.count("/")
        
        
        if count_numerical_value == 1 and not (any(x.isalpha() for x in numerical_value)):
            slash_position = numerical_value.find("/")
            numerical_value = float(numerical_value[0:slash_position])/float(numerical_value[slash_position+1:])
        
        try:
            numerical_value = float(numerical_value)
        except ValueError:
            raise Exception("Apenas valores numéricos são permitidos")
        
        return numerical_value
        
        
        
            

        

class Seventh_Question:

    def __init__(self):
        self.PG = []
        
        print("Selecione os valores que deseja adicionar na array, quando concluir pressione Enter.")
        
        
        
        while 1:
            numerical_value = input()
            count_numerical_value = numerical_value.count("/")
            
            
            if count_numerical_value == 1 and not (any(x.isalpha() for x in numerical_value)):
                slash_position = numerical_value.find("/")
                numerical_value = float(numerical_value[0:slash_position])/float(numerical_value[slash_position+1:])
            
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numéricos são permitidos")
                else:
                    break
                
            
            self.PG.append(numerical_value)
        
        if len(self.PG) == 0:
            raise Exception("Sem valores existentes na array.")
    
        if len(self.PG) > 0 and len(self.PG) < 3:
            raise Exception("Valores insuficientes na array.")

    
        
        
    def Calculate(self):
        
        flag_zero = 0
        flag_value = round(self.PG[1]/self.PG[0], 4)
        
        if (self.PG[0] != 0 and all(x==0 for x in self.PG[1:])):
            print("É uma P.G estacionária.")
            flag_zero = 1
        
        if flag_zero == 0:
            for i in range(2, len(self.PG)):
                
                if self.PG[i-1] == 0:
                    self.PG[i-1] = 1
                    
                
                if (round(self.PG[i]/self.PG[i-1], 4)) == flag_value:
                    continue
                else:
                    raise Exception("Não é uma P.G.")
             

            if (self.PG[0] > 0 and self.PG[1] < 0) or (self.PG[0] < 0 and self.PG[1] > 0):
                print("É uma P.G alternante.")
                
            else:
                if flag_value > 1:
                    print("É uma P.G crescente.")
                if flag_value < 1:
                    print("É uma P.G decrescente.")
                if flag_value == 0:
                    print("É uma P.G constante.")
        


class Eighth_Question:
    def __init__(self):
        self.value1 = self.stringValidation("Insira o valor inicial da P.G:")
        self.value2 = self.stringValidation("Insira o valor final da P.G:")
        self.K = self.stringValidation("Insira a razão da P.G:")
        
        if self.value1 > self.value2:
            self.flag = 1 #Crescente

        if self.value1 < self.value2:
            self.flag = 0 #Decrescente 
        
    def Calculate(self):
        i = 0
        array = [self.value1]
        
        if self.flag == 1:
            while array[i]*self.K > self.value2:
                array.append(array[i]*self.K)
                i+=1
        
        else:
            while array[i]*self.K < self.value2:
                array.append(array[i]*self.K)
                i+=1      
        
        array.append(self.value2)
        print(array)
    
    
    def stringValidation(self, text):
        numerical_value = input(text)
        count_numerical_value = numerical_value.count("/")
        
        
        if count_numerical_value == 1 and not (any(x.isalpha() for x in numerical_value)):
            slash_position = numerical_value.find("/")
            numerical_value = float(numerical_value[0:slash_position])/float(numerical_value[slash_position+1:])
        
        try:
            numerical_value = float(numerical_value)
        except ValueError:
            raise Exception("Apenas valores numéricos são permitidos")
        
        return numerical_value
        



class Nineth_Question:

    def __init__(self):
        self.PG = []
        
        print("Selecione os valores que deseja adicionar na array, quando concluir pressione Enter.")
        
        
        
        while 1:
            numerical_value = input()
            count_numerical_value = numerical_value.count("/")
            
            
            if count_numerical_value == 1 and not (any(x.isalpha() for x in numerical_value)):
                slash_position = numerical_value.find("/")
                numerical_value = float(numerical_value[0:slash_position])/float(numerical_value[slash_position+1:])
            
            try:
                numerical_value = float(numerical_value)
            except ValueError:
                if numerical_value != "":
                    raise Exception("Apenas valores numéricos são permitidos")
                else:
                    break
                
            
            self.PG.append(numerical_value)
        
        if len(self.PG) == 0:
            raise Exception("Sem valores existentes na array.")
    
        if len(self.PG) > 0 and len(self.PG) < 3:
            raise Exception("Valores insuficientes na array.")
    
    def Calculate(self):
        r = self.PG[1]/self.PG[0]

        for i in range(2, len(self.PG)):
            
            if self.PG[i-1] == 0:
                self.PG[i-1] = 1
                
            
            if (self.PG[i]/self.PG[i-1]) == r:
                continue
            else:
                raise Exception("Não é uma P.G.")
        
        print("A soma dos termos da P.G é:", (self.PG[0]*(r**(len(self.PG)))-self.PG[0])/(r-1))
        print("O produto dos termos da P.G é:", (self.PG[0]**len(self.PG))*(r**((len(self.PG)*(len(self.PG)-1))/2)))




class Menu:
    def __init__(self):
        
        questoes = ["Primeira", "Segunda", "Quinta", "Sétima", "Oitava", "Nona"]
        
        dict_questoes = {"Primeira": First_Question, "Segunda":Second_Question, "Quinta":Fifth_Question,
                         "Sétima":Seventh_Question, "Oitava":Eighth_Question, "Nona":Nineth_Question}
        
        for i in range(len(questoes)):
            print(questoes[i] + " Questao - " + str(i))
        
        self.select = input("Selecione a questão:")
        
        
        try:
            self.select = int(self.select)
        
        except:
            raise Exception("Apenas valores numericos inteiros sao permitidos.")
        
        if self.select > 5:
            raise Exception("Valor fora dos mencionados.")
        
        
        
        if self.select != 0:
            dict_questoes[questoes[self.select]]().Calculate()
        else:
            dict_questoes[questoes[self.select]]()
            
        
        



Menu()





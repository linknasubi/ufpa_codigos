class Question_1:
    def __init__(self, n):
        self.n = n
        
    
    def findPrime(self):
        
        check = True
        
        for i in range(2, int(self.n**(1/2))+1):
            check = check and self.n%i != 0            
        
        return check


class Question_2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    
    def findMDC(self):
        r = 0
        dic = {'Primos Entre Si': False, 'MDC':0}
        
        
        while(self.b != 0):
            r = self.a % self.b
            self.a = self.b
            self.b = r
        
        if self.a == 1:
            dic['Primos Entre Si'] = True
            
        dic['MDC'] = self.a
        

            
            
        return dic
    

class Question_3:
    def __init__(self, p):
        self.p = p
        
    def primesCheck(self):
        array = []
        prime = False
        
        for i in range(1, self.p, 2):
            prime = Question_1(i).findPrime()
            
            if(prime == True):
                array.append(i)

        
        return array
    


class Question_4:
    def __init__(self, p):
        self.p = p
        
    def primesCheck(self):
        array = []
        prime = False
        primeCounter = 0
        i = 0
        
        while(primeCounter < self.p):
            i += 1
            prime = Question_1(i).findPrime()
            
            if(prime == True):
                array.append(i)

                primeCounter += 1
        
        return array



class Question_5:
    def __init__(self, n):
        self.n = n
        
    def fatoNum(self):
        
        value = 2
        dic = {}
        
        while self.n != 1:
            
            
            if(self.n % value == 0):
                
                try:
                    dic[value] += 1
                
                except KeyError:
                    dic[value] = 0
                    dic[value] += 1
                
                
                self.n = self.n / value
                
            else:
                
                value += 1
        
        
        aux = 0
        for key, value in dic.items():
            aux += 1
            
            if(aux < len(dic)):
                print(str(key)+"^("+str(value)+")", end = ' * ')
            else:
                print(str(key)+"^("+str(value)+")\n")
            
        
        return dic


        

   
class Question_6:
    def __init__(self):
        self.array = []
        for i in range(1, 14):
            self.array.append( ( i**2 ) + (29*i) + 101) 


class Question_7:
    
    def __init__(self, a, m):
        self.a = a
        self.m = m
        self.array = []
        
    
    def betwPrimesCheck(self, b):

        prime = {}
        primeCounter = 0
        

        
        while(primeCounter < 10):
            
            b += 1
            prime = Question_2(self.a, b).findMDC()
            
            if(prime['Primos Entre Si'] == True):
                
                self.array.append(b)
                primeCounter += 1
        
        return self.array, b
        
        
    def checkProperty(self):
        
        marker = 1
        mdc = Question_2(self.a, self.m).findMDC()
        
        if mdc['Primos Entre Si'] == False:
            return print('A propriedade nao foi atendida.\n')
        
        else:
            while True:
                
                array = self.betwPrimesCheck(marker)
                marker = array[1]
                array = array[0]
                

                for i in range(len(array)):
                    
                    if( ( (self.a * array[i]) % self.m ) == 1):
                        
                        return array[i]
                
   
    

import random

class Question_8:
    
    
    
    def __init__(self, p, q, message):
        self.p = p
        self.q = q
        self.message = message
        
        print('Chave Privada: ' + str(self.p) +' e '+ str(self.q))
        
    
    def RSA(self):
        
        dic = {}
        
        N = self.p * self.q
        Phi = (self.p-1) * (self.q - 1)
        E = 0
        
        E_array = []
        
        
        for i in range(2, Phi):
            E = Question_2(i, Phi).findMDC()
            
            if(E['Primos Entre Si'] == True):
                E_array.append(i)
                
        E = random.choice(E_array)
        

        print('Chave Pública: ' + str(N) +' e '+ str(E))
        
        code = list(bytes(f'{self.message}'.encode()))
        new_code = []
        
        
        for i in code:
            new_code.append( ( i**(E) ) % N )
            
        
        dic['Privado'] = [self.p, self.q]
        dic['Publico'] = [N, E]
        dic['Codificado'] = ''.join(chr(i) for i in new_code)
        
        
        print('Codificado: ' + ''.join(chr(i) for i in new_code))
        
        D = Question_7(E, Phi).checkProperty()
        
        dic['Decodificado'] = ''.join(chr( ( i ** D ) % N ) for i in new_code)
        
        
        print(dic['Decodificado'] + '\n')
        
        return dic
        
        
        
        
        
        




first = Question_1(67).findPrime()
second = Question_2(3, 5).findMDC()
third = Question_3(15).primesCheck()
fourth = Question_4(5).primesCheck()
fifth = Question_5(1000000).fatoNum()
sixth = Question_6().array
seventh = Question_7(13, 640).checkProperty()

eighth_0 = Question_8(53, 67, 'UFPA').RSA()
eighth_1 = Question_8(53, 67, 'ICEN').RSA()
eighth_2 = Question_8(53, 67, 'FACOMP').RSA()



















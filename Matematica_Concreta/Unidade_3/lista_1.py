class Pascal:
    def __init__(self, n):
        self.n = n+1
        
        self.array = [[1], [1,1]]
        

    
    def triangleMaker(self):
        
        for i in range(2, self.n):
            self.array.append([1])

            for j in range(i-1):
                self.array[i].append(self.array[i-1][j] + self.array[i-1][j+1])


            self.array[i].append(1)



        return self.array
    

class Arranjo:
    def __init__(self, r):
        
        self.r = r
        self.array = []
    
    
    
    def binMaker(self, value):
        aux = bin(value)[2:]
        if len(aux) < self.r:
            aux = '0'*(self.r-len(aux))+aux
        
        return aux
    
    def combMaker(self):
        for i in range(2**self.r):
            self.array.append(self.binMaker(i))
            
        return self.array







class Combinatoria:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        
    
    
    def combCalc(self):
        result_n = 1
        result_p = 1
        
        for i in range(self.n, self.n-self.p, -1):
            result_n *= i 
        
        for i in range(self.p, 0, -1):
            result_p *= i
            
        return result_n//result_p





class BiNewton(Pascal):
    def __init__(self, r):
        self.r = r
        super().__init__(self.r)
        self.pascal_tri = self.triangleMaker()

    
    def calcNewton(self):
        
        i = self.r+1
        j = -1
        string_bin = str()
        
        
        for k in self.pascal_tri[self.r]:
            
            i -= 1
            j += 1
            
            if i == 0:             
                string_bin += 'a^'+str(j) 
            
            if j == 0:
                string_bin += 'x^'+str(i)+' + '
            
            if i == 1 and j != 1:
                string_bin += str(k) + 'x'+'a^'+str(j) + ' + '
                
            if j == 1 and i != 1:
                string_bin += str(k) + 'x^'+str(i)+'a' + ' + '
            
            if j==1 and i==1:
                string_bin += str(k) + 'x'+'a' + ' + '
            
            
            if i>1 and j>1:
                string_bin += str(k) + 'x^'+str(i)+'a^'+str(j) + ' + '
                
            
        
        return string_bin


pascal = Pascal(6).triangleMaker()

arranjo = Arranjo(2).combMaker()


combinatoria = Combinatoria(5,5).combCalc()


newton = BiNewton(2).calcNewton()




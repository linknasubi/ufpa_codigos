class Prime(object):
    def __init__(self, N):
        self.N = N
        self.flag = 0
        
        if (self.N % 2) == 0:
            self.flag = 1
        
        else:         
            for i in range(3, self.N, 2):
                if self.flag == 0:
                    if (self.N % i) == 0:
                        self.flag = 1
                else:
                    break



class Second_Question(Prime):
    def __init__(self, N):
        self.N = N
        
        super().__init__(self.N)
        
        if self.flag == 0:
            print("Primo.")
        else:
            print("Nao primo.")


class Third_Question(Prime):
    def __init__(self, N_2):
        self.N_2 = N_2
    
    
    def primeCheck(self):
        prim_seq = [2]
        
        if (self.N_2 % 2) == 0:
            self.N_2 = self.N_2 - 1
        
        for i in range(self.N_2, 1, -2):
            super().__init__(i)
            
            if self.flag == 0:
                prim_seq.append(i)
        
        print(prim_seq)
                
        
        


Second_Question(5)

Third_Question(5).primeCheck()
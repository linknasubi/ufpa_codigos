class Process:
    def __init__(self, TS, TotalTime, Priority, name):
        self.TS = TS
        self.TT = TotalTime
        self.PR = Priority
        self.name = name
        
    
    def executeProcess(self):
        self.TT -= self.TS




class Rounding:
    
    def __init__(self, items):
        
        self.line = []
        
        if(len(items) != 0):
            for i in range(len(items)):
                self.line.append(items[i])
        
            
    
    def lastPositioning(self):

        self.line.append(self.line.pop(0))
        
        
    def removeElement(self, key):
        self.line.pop(key)
        
        
    def appendElement(self, item):
        self.line[item[0]] = item[1]
        
    def returnLine(self):
        return self.line






class RoundRobin:
    
    def __init__(self, TS, processes):
        self.TS = TS
        self.processes = []
        
        for i in range(len(processes)):
            self.processes.append(  Process(TS, processes[i], 0, 'P'+str(i)) )
        
        
        self.line = Rounding(self.processes)

        
    
    def runningManager(self):
            

        line = self.line.line

 
        while len(line) > 0:
            
            self.GUI()
            
            value = line[0]
            
            value.executeProcess()


            if(value.TT <= 0):
                
                self.line.removeElement(0)
                
            
            if(len(line) > 0):
                self.line.lastPositioning()
                
    
    
                    
    
    def GUI(self):
        
        line = self.line.line
        
        aux = 0
        
        print('')
        
        
        
        for i in line:
            
            value = i.TT
            key = i.name
            
            if aux == 0:
            
                if value > self.TS:
                    print(key + ', ' +  str(self.TS) + '; ', end='')
                
                else:
                    print(key + ', ' +  str(value) + '*; ', end='')
                    
            else:
                print(key + ', 0' + '; ', end='')
            
            aux += 1
            





class FIFO:
    
    def __init__(self, TS, processes):
        
        self.TS = TS
        self.PA = []                   #Priority Array
        self.line_array = []

        
        for i in range(10):                 #Allocate space to all priority arrays
            self.PA.append([])

        
        
        for i in range(len(processes)):  #Assigns each process to its priority queue
            
            priority = processes[i][1]
            total_time = processes[i][0]
            
            process = Process(self.TS, total_time, priority, 'P'+str(i))
            
            
            self.PA[priority].append(process)
            
        
        for i in range(len(self.PA)):              #Assigns each priority array to Rounding object
            
            
            self.line_array.append( Rounding( self.PA[i] )   )
            
    
    
    def runningManager(self):
        
        actual_pr = -1
        
        while actual_pr < len(self.PA)-1:
            
            actual_pr += 1
            
            line = self.line_array[actual_pr]
            
            while len(line.line) > 0:
                
        
                self.GUI(line.line)
                
                value = line.line[0]
                
                value.executeProcess()
    
    
                if(value.TT <= 0):
                    
                    line.removeElement(0)
                    
                
                if(len(line.line) > 0):
                    line.lastPositioning()
            
        
    
    def GUI(self, line):
        
        
        print('')
        
        aux = 0
        
        for i in line:
            
            value = i.TT
            key = i.name
            
            if aux == 0:
                if value > self.TS:
                    print(key + ', ' +  str(self.TS) + '; ', end='')
                
                else:
                    print(key + ', ' +  str(value) + '*; ', end='')
            
            else:
                print(key + ', 0' +  '; ', end='')
            
            
            aux += 1
        
        
        
        
            



RoundRobin(5, [   50,  51, 28, 10, 87   ]).runningManager()

FIFO(10, [   [100, 7],  [51, 2], [28, 7], [11, 0], [157, 5]   ]).runningManager()





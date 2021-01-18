import time


class Mtrx_Graph:
    
    """
        Last element assigned in each matrix row is assigned to its loop number.
        Penult element assigned in each matrix row is assigned to its degree.
    """
    
    def __init__(self, V):
        
        self.V = V
        self.A = 0
        self.Matrix = []
        Matrix_aux = []
        
        
        for i in range(0, self.V):
            for j in range(0, self.V):
                Matrix_aux.append(0)
            self.Matrix.append(Matrix_aux)
            self.Matrix[i].append([0,0])
            Matrix_aux = []
    
    """
        Edge will be created between consecutive node values, number of elements must be even.
    """
    def addEdge(self, EdgePoints, Oriented:int):
        
        self.A = len(EdgePoints)//2

        for i in range(0, len(EdgePoints), 2):
            self.Matrix[EdgePoints[i]][EdgePoints[i+1]] = 1
            
            
            if EdgePoints[i] != EdgePoints[i+1]:
                self.Matrix[EdgePoints[i]][-1][0] += 1
            else:
                self.Matrix[EdgePoints[i]][-1][1] = 1  
                self.Matrix[EdgePoints[i]][-1][0] += 2    
            
        
        if Oriented == 0:
            for i in range(0, len(EdgePoints), 2):
                self.Matrix[EdgePoints[i+1]][EdgePoints[i]] = 1

            
            
    
    def nodeDegree(self, Node):
        
        return self.Matrix[Node][-1][0]
    
    def maxDegree(self):
        aux = 0
        
        for i in range(len(self.Matrix)):
            if self.Matrix[i][-1][0] > aux:
                aux = self.Matrix[i][-1][0]
        
        return aux
        
    
    def edges(self):
        return self.A
    
    
    def nodes(self):
        return self.V
    
    def loopCount(self):
        aux = 0
        for i in range(len(self.Matrix)):
            aux += self.Matrix[i][-1][1]
        
        return aux
    
    
    
class ListAdj_Graph:
    def __init__(self, V:list):
        self.A = 0
        self.V = V
        self.loop = 0
        self.graph = {}
        for i in self.V:
            self.graph[i] = []
            
    
    def addEdge(self, EdgePoints:list, Oriented):
        
        self.A = len(EdgePoints)//2
        
        for i in range(0, len(EdgePoints), 2):
            
            self.graph[EdgePoints[i]].append(EdgePoints[i+1])
            
            
            if EdgePoints[i] == EdgePoints[i+1]:
                self.loop += 1
                
                
        if Oriented == 0:
            
            for i in range(0, len(EdgePoints), 2):
                if EdgePoints[i+1] != EdgePoints[i]:
                    self.graph[EdgePoints[i+1]].append(EdgePoints[i])
        

        
    def nodeDegree(self, Node):
        
        return len(self.graph[Node])
    
    
    
    def maxDegree(self):
        aux = 0
        
        for i in self.graph:
            if len(i) > aux:
                aux = len(i)
        
        return aux
        
    
    def edges(self):
        return self.A
    
    
    def nodes(self):
        return len(self.graph)
    
    def loopCount(self):
        aux = 0
        for i in range(len(self.graph)):
            aux += self.Matrix[i][-1][1]
        
        return aux



graphs = ListAdj_Graph([1,2,3,4,5,6, 7]) 

#Creates edges, the last value points to a oriented graph or non oriented.
graphs.addEdge([1,2, 1,5, 1,6, 2,3, 3,4, 3,7, 4,5, 6,3, 6,7], 1)


graphs_values = graphs.graph





class DFS:


    def __init__(self, graph):
        
        
        self.time_stamp = {}
        self.white = []
        self.gray = []
        self.black = []
        self.graph = graph
        self.sort_topography = []
        
        self.id = -1
        self.id_comp = []
        
        for i in (self.graph):
            self.white.append(i)
            self.time_stamp[i] = time.time()
        
        for i in (self.graph):
            if i in self.white:
                
                self.id += 1
                self.id_comp.append([])
                
                
                self.checkGraph(i)
    


    def checkGraph(self, i):

        
        self.gray.append(i)
        self.white.remove(i)
        
        


        
        for j in self.graph[i]:
            if j in self.white:
                self.checkGraph(j)
                
        self.sort_topography.append(i)
        
        
        print("Gray List ->", self.gray, "////","Black List ->", self.black, "\n")
        self.gray.remove(i)
        self.black.append(i)
        self.time_stamp[i] -= time.time()
        self.time_stamp[i] *= -1
        
        


dfs = DFS(graphs_values)

# for i in range(len(dfs.id_comp)):
#     print("Component "+str(i), dfs.id_comp[i])
    

counter = 0
for i in (dfs.sort_topography[::-1]):
    if counter < len(dfs.sort_topography[::-1])-1:
        
        print('', i, "\n |\n"+" |\n"+"\ /")
        
    else:
        
        print('',i)

    counter += 1
    
    



class BFS:
    
    def __init__(self, graph):
        
        self.white = []
        self.black = []
        self.graph = graph
        
        
        for i in (self.graph):
            self.white.append(i)
            
        self.line = [self.white[0]]
        print(self.line)
    
    def checkGraph(self):
        
        while self.white != []:
            
            if self.line == []:
                self.line.append(self.white[0])
        
            self.white.remove(self.line[0])
            
            
            
            for i in self.graph[self.line[0]]:
                if i in self.white and i not in self.line:
                    self.line.append(i)
                    
            
            
            self.black.append(self.line[0])
            self.line.pop(0)
            
            
            print("Line -> ", self.line, "///////", "Black List ->", self.black)
            
            
        
        
        

# bfs = BFS(graphs_values)
# bfs.checkGraph()




















            
        
        
        
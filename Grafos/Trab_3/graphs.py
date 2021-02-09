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
        self.weight = {}
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
    
    def deleteEdge(self, EdgePoints:list):
        for i in range(0, len(EdgePoints), 2):
            self.graph[EdgePoints[i]].remove(EdgePoints[i+1])
            self.graph[EdgePoints[i+1]].remove(EdgePoints[i])
            
        
    def addNode(self, nodes:list):
        self.V += nodes
        
        for i in self.V:
            self.graph[i] = []

    
    def deleteNode(self, nodes:list):
        for i in nodes:
            del self.graph[i]
            self.V.remove(i)
        
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
    
    
    
    
    def weightAssign(self, key_val):
        
        
        for i in key_val:
            
            arr = i.split(",")
            arr[0] = int(arr[0])
            arr[1] = int(arr[1])
            
            if(arr[1] in self.graph or arr[1] in self.graph):
                self.weight = key_val
            else:
                print("Non existent edge in edge set")
                
                
    
                
class MST:
    
    def __init__(self, graph, weights):
        self.graph = graph
        self.weight = weights
        self.new_graph = ListAdj_Graph(graph.keys())
        
    
    def executeMST(self):
        
        counter = 0
        totalSum = 0
        
        new_weight = dict(sorted(self.weight.items(), key=lambda item: item[1]))
        
        
    
        for key, value in new_weight.items():
            
            arr = key.split(',')
            
        
            self.new_graph.addEdge( [ int(arr[0]), int(arr[1]) ], 0)
            
            if(DFS(self.new_graph.graph).callingCycleDetection( int(arr[0]))):
    
                self.new_graph.deleteEdge([ int(arr[0]), int(arr[1]) ])
            
            else:    
                
                print("\nAdding edges:", key, "that weights", value)
                print('')
                print("Adjacency Graph: ", self.new_graph.graph)
                
                totalSum += value        
                counter += 1

                
                if counter == len(self.graph)-1:
                    break
        
        print("\n The total sum is:", totalSum)
        return self.new_graph.graph
            
            
            


class DFS:


    def __init__(self, graph):
        
        
        self.time_stamp = {}
        self.white = []
        self.gray = []
        self.black = []
        self.graph = graph
        self.sort_topography = []
        
        self.bool = False
        
        self.id = -1
        self.id_comp = []
        
        for i in (self.graph):
            self.white.append(i)
            self.time_stamp[i] = time.time()
        
    
    
    def callingCycleDetection(self, i):
        
        value = False
        
        if i in self.white:
            value = self.cycleDetection(i, i)
    
        
        return value    
    
    def callingCheckGraph(self):

        
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
    
    
    def cycleDetection(self, i, parent):
        
        self.gray.append(i)
        self.white.remove(i)
        
        for j in self.graph[i]:
            if j in self.white:
                self.cycleDetection(j, i)
            
            elif (j != parent):
                self.bool = True

            
            
        return self.bool
                

                
        
        
        print("Gray List ->", self.gray, "////","Black List ->", self.black, "\n")
        self.gray.remove(i)
        self.black.append(i)
        self.time_stamp[i] -= time.time()
        self.time_stamp[i] *= -1
        





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
            
            
        
        

graphs = ListAdj_Graph([1,2,3,4,5,6,7,8,9]) 


#Creates edges, the last value points to a oriented graph or non oriented.
graphs.addEdge([1,2, 2,3, 3,4, 4,5, 5,6, 6,7, 7,8, 8,1, 2,8, 9,3, 9,8, 9,7, 4,6, 3,6], 0)

graphs.weightAssign({"1,2":4, "2,3":8,"3,4":7, "4,5":9,"5,6":10, "6,7":2,"7,8":1, "8,1":8,"2,8":11,
                     "9,3":2,"9,8":7, "9,7":6,"4,6":14, "3,6":4})

graphs_weights = graphs.weight
graphs_values = graphs.graph

tree = MST(graphs_values, graphs_weights).executeMST()



















            
        
        
        
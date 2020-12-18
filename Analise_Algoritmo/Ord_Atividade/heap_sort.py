
class HeapSort:
    def __init__(self, array):
        self.array = array
        
        self.maxHeap(self.array)
        
            
        
        
    def maxHeap(self, array):
        
        n = len(array)
        
        for i in range(n//2 - 1, -1, -1):
            self.searchHeap(array, n, i)
        
        for i in range(n-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.searchHeap(array, i, 0)
        
    
    
    def searchHeap(self, array, n, i):
        
        left = (i*2) + 1
        right = (i*2) + 2
        

        
        greater = i
        
        if left <= n and self.array[i] < self.array[left]:
            greater = left
        
        if right <= n and self.array[i] < self.array[right]:
            greater = right
        
        
        if greater != i:
            self.array[i], self.array[greater] = self.array[greater], self.array[i]
            self.searchHeap(self.array, n, greater)
        

array = [4,52,6,3,3,1,53,32,2,1,5,7,8]
heap = HeapSort(array)
print(heap.array)

# class QuickSort:
#     def __init__(self):

#         pass
    
    
#     def partQuick(self, array, initial, array_len):
#         x = array[array_len]
#         i = initial-1
        
#         for j in range(initial, array_len):
#             if array[j] <= x:
#                 i += 1
#                 array[i], array[j] = array[j], array[i]
                
#         array[i+1], array[array_len] = array[array_len], array[i+1]
        
#         return i+1
        
    
    
#     def recQuick(self, array, initial, array_len):
#         if initial < array_len:
#             q = self.partQuick(array, initial, array_len)
#             self.recQuick(array, initial, q-1)
#             self.recQuick(array, q+1, array_len)
        
#         print(array)
    
# array = [5,3,6,1,72,2,15,7,123,42,78,2]
# teste = QuickSort()
# teste.recQuick(array, 0, len(array)-1)



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






























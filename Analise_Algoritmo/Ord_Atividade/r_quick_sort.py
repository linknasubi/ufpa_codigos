import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

class rQuickSort:
    
    def __init__(self, print_flag):

        self.print_flag = print_flag
    
    
    def partition(self, arr, low, high):
     
        pivot = arr[random.randint(low, high)]
        j = high + 1
        i = low - 1
     
        while 1:
     
            i += 1
            while (arr[i] < pivot):
                i += 1
     
            j -= 1
            while (arr[j] > pivot):
                j -= 1

            if (i >= j):
                return j
     
            arr[i], arr[j] = arr[j], arr[i]
            
            if self.print_flag == 1:
                
                print(arr)
     
     
     
    def quickSort(self, arr, low, high):
        ''' pi is partitioning index, arr[p] is now 
        at right place '''
        if (low < high):
     
            pivot = self.partition(arr, low, high)
            
            self.quickSort(arr, low, pivot)
            self.quickSort(arr, pivot + 1, high)



"""

LETRA D.A

"""

array = []

for i in range(0,20):
    

    array.append(random.randint(1,100))



quick = rQuickSort(1)
quick.quickSort(array, 0, len(array)-1)


print(array)


"""

LETRA D.B


"""










"""

LETRA D.C


"""



def arraysGen(first_array, size):


    #first_array = []
    time_list = []
    
    
    for i in range(0,size):
        
        first_array.append(random.randint(1,1000))
    
    
    sort_array  = sorted(first_array)
    
    
    time_list.append(time.time())
    
    rQuickSort(0).quickSort(sort_array, 0, len(sort_array)-1)
    
    time_list[0] = abs(time_list[0] - time.time())
    
    
    
    
    
    sort_inv_array = sorted(first_array, reverse=True)
    
    
    time_list.append(time.time())
    
    rQuickSort(0).quickSort(sort_inv_array, 0, len(sort_inv_array)-1)
    
    time_list[1] = abs(time_list[1] - time.time())
    
    
    
    
    time_list.append(time.time())
    
    rQuickSort(0).quickSort(first_array, 0, len(first_array)-1)
    
    time_list[2] = abs(time_list[2] - time.time())
    
    
    
    return first_array, time_list

time_list = arraysGen([], 60000)
array_list = time_list[0]
time_list = time_list[1]


fig = plt.figure()
label = ['Crescente', 'Decrescente', 'Desordenada']
all_time = [time_list[0], time_list[1], time_list[2]]
plt.bar(label,all_time)
plt.ylabel('Tempo')
plt.title('Pivô Aleatório')
plt.savefig("bar_random_quick.png",dpi=100)
plt.show()



timing_sorted = []
timing_inv_sorted = []
timing_unordered = []

sizes = []

for i in range(300,700, 10):
    sizes.append(i)
    
    quick_gen = arraysGen(array_list, i)
    
    array_list = quick_gen[0]
    
    timing_sorted.append(quick_gen[1][0])
    timing_inv_sorted.append(quick_gen[1][1])
    timing_unordered.append(quick_gen[1][2])
    


plt.plot(sizes, timing_sorted)
plt.plot(sizes, timing_inv_sorted)
plt.plot(sizes, timing_unordered)

plt.legend(['Ordenado Crescente', 'Ordenado Decrescente', 'Desordenado'], loc='upper left')
plt.title('Pivô Aleatório')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo')
plt.savefig("plot_random_quick.png",dpi=100)

plt.show()























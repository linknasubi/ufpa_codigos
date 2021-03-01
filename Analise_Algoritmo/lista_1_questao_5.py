import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import six
import random
import time

class rQuickSort:
    
    def __init__(self):
        pass
    
    
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
            

     
     
    def quickSort(self, arr, low, high):
        ''' pi is partitioning index, arr[p] is now 
        at right place '''
        if (low < high):
     
            pivot = self.partition(arr, low, high)
            
            self.quickSort(arr, low, pivot)
            self.quickSort(arr, pivot + 1, high)




def selection_sort(nums):
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    
    return nums

rand_value_range = 1
rand_list_range = [rand_value_range]
random_values_list = []

ord_list_range = [1]
ord_values_list = []

for i in range(0,17):
    
    random_values = random.sample(range(0,1000000), rand_value_range)
    random_values_list.append(random_values)
    rand_value_range *= 2
    rand_list_range.append(rand_value_range)


for i in range(0,17):
    ord_values_list.append([])
    for j in range(0, ord_list_range[i]):
        ord_values_list[i].append(j)
    
    ord_list_range.append(ord_list_range[i]*2)


random_list = random_values_list[:]
ord_list = ord_values_list[:]


time_list = []

select_seq = [[], []]
quick_seq = [[] , []]





for i in range(len(random_list)):
    init_time = time.time()
    random_list_of_nums = rQuickSort().quickSort(random_list[i], 0, len(random_list[i])-1)
    quick_seq[0].append(round(time.time() - init_time, 4))
    quick_seq[1].append(len(random_list[i]))

            

for i in range(len(random_list)):

    init_time = time.time()
    random_list_of_nums = selection_sort(random_list[i])
    select_seq[0].append(round(time.time() - init_time, 4))
    select_seq[1].append(len(random_list[i]))

print(select_seq)



def plotting(range_size, time_value, name):

    plt.figure(figsize = (10,8))
    plt.xlabel('Tamanho de entrada.')
    plt.ylabel('Tempo em segundo.')
    plt.title(name)
    plt.plot(range_size, time_value, "-r", label="Valores aleatórios")
    plt.legend(loc="upper left")
    plt.savefig("./lista_1_quest_5/"+name+"_1")
    plt.show()


plotting(select_seq[1], select_seq[0], "Selection")
plotting(quick_seq[1], quick_seq[0], "Quick")


def tabling(range_size, time_value, name):
    df = pd.DataFrame()
    df['Entrada'] = range_size

    df['Segundos'] = time_value
    
    return df





def render_mpl_table(data, col_width=5.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax


#
#
#
#plotting(insert_seq[0], insert_seq[1], "Algoritmo de inserção.")
#plotting(bubble_seq[0], bubble_seq[1], "Algoritmo bolha.")
#plotting(select_seq[0], select_seq[1], "Algoritmo de seleção.")
#
#
render_mpl_table(tabling(select_seq[1], select_seq[0], "Selection"), header_columns=0, col_width=2.0)
render_mpl_table(tabling(quick_seq[1], quick_seq[0], "Quick"), header_columns=0, col_width=2.0)




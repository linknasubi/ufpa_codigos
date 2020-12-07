import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import six
import random
import time

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    
    return nums



def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert
        
    return nums




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

for i in range(0,15):
    
    random_values = random.sample(range(0,1000000), rand_value_range)
    random_values_list.append(random_values)
    rand_value_range *= 2
    rand_list_range.append(rand_value_range)


for i in range(0,15):
    ord_values_list.append([])
    for j in range(0, ord_list_range[i]):
        ord_values_list[i].append(j)
    
    ord_list_range.append(ord_list_range[i]*2)


random_list = random_values_list[:]
ord_list = ord_values_list[:]


time_list = []

insert_seq = [[ [], [] ], []]
bubble_seq = [[ [], [] ], []]
select_seq = [[ [], [] ], []]


for j in range(2):

    for i in range(len(random_list)):
        if j == 0:
            init_time = time.time()
            random_list_of_nums = insertion_sort(random_list[i])
            insert_seq[0][0].append(round(time.time() - init_time, 4))
        else:
            init_time = time.time()
            ord_list_of_nums = insertion_sort(ord_list[i])
            insert_seq[0][1].append(round(time.time() - init_time, 4))
        
            insert_seq[1].append(len(random_list[i]))


    for i in range(len(random_list)):
        if j == 0:
            init_time = time.time()
            random_list_of_nums = bubble_sort(random_list[i])
            bubble_seq[0][0].append(round(time.time() - init_time, 4))
        else:
            init_time = time.time()
            ord_list_of_nums = bubble_sort(ord_list[i])
            bubble_seq[0][1].append(round(time.time() - init_time, 4))
            
            bubble_seq[1].append(len(random_list[i]))
            

    for i in range(len(random_list)):
        if j == 0:
            init_time = time.time()
            random_list_of_nums = selection_sort(random_list[i])
            select_seq[0][0].append(round(time.time() - init_time, 4))
        else:
            init_time = time.time()
            ord_list_of_nums = selection_sort(ord_list[i])
            select_seq[0][1].append(round(time.time() - init_time, 4))
        
            select_seq[1].append(len(random_list[i]))









def plotting(range_size, time_value, name):

    plt.figure(figsize = (10,8))
    plt.xlabel('Tamanho de entrada.')
    plt.ylabel('Tempo em segundo.')
    plt.title(name)
    plt.plot(range_size, time_value[1], "-g", label="Valores ordenados")
    plt.plot(range_size, time_value[0], "-r", label="Valores aleatórios")
    plt.legend(loc="upper left")
    plt.savefig("./lista_1_quest_5/"+name+"_1")
    plt.show()


plotting(select_seq[1], select_seq[0], "Selection")
plotting(insert_seq[1], insert_seq[0], "Insertion")
plotting(bubble_seq[1], bubble_seq[0], "Bubble")


def tabling(range_size, time_value, name):
    df = pd.DataFrame()
    df['Entrada'] = range_size
    df['Ordenados'] = time_value[0]
    df['Aleatórios'] = time_value[1]
    
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
render_mpl_table(tabling(insert_seq[1], insert_seq[0], "Insertion"), header_columns=0, col_width=2.0)
render_mpl_table(tabling(bubble_seq[1], bubble_seq[0], "Bubble"), header_columns=0, col_width=2.0)



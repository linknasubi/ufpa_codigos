import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import six


range_size = []

insert_seq = [[], []]
bubble_seq = [[], []]
select_seq = [[], []]

for i in range(1,15):
    range_size.append(i)
    insert_seq[0].append(i**2)
    insert_seq[1].append(i)
    


for i in range(1,15):
    bubble_seq[0].append(i**2)
    bubble_seq[1].append(i)
    

for i in range(1,15):
    select_seq[0].append(i**2)
    select_seq[1].append(i**2)



def plotting(array_worst, array_best, name):

    plt.figure(figsize = (10,5))
    plt.xlabel('Tamanho de entrada.')
    plt.ylabel('Instruções.')
    plt.title(name)
    plt.plot(range_size, array_worst, "-g", label="Melhor caso.")
    plt.plot(range_size, array_best, "-r", label="Pior caso.")
    plt.legend(loc="upper left")
    plt.savefig("./lista_1_quest_5/"+name)
    plt.show()



def tabling(array_worst, array_best, name):
    df = pd.DataFrame()
    df['Entrada'] = range_size
    df['Pior Caso'] = array_worst
    df['Melhor Caso'] = array_best
    
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





plotting(insert_seq[0], insert_seq[1], "Algoritmo de inserção.")
plotting(bubble_seq[0], bubble_seq[1], "Algoritmo bolha.")
plotting(select_seq[0], select_seq[1], "Algoritmo de seleção.")


render_mpl_table(tabling(insert_seq[0], insert_seq[1], "a"), header_columns=0, col_width=2.0)
render_mpl_table(tabling(bubble_seq[0], bubble_seq[1], "a"), header_columns=0, col_width=2.0)
render_mpl_table(tabling(select_seq[0], select_seq[1], "a"), header_columns=0, col_width=2.0)





#fig = plt.figure(figsize=(10,5))
#plt.scatter(teste2[:,0], teste2[:,1], c=data_color, s = 50)
#plt.savefig("./Results/Breasts_Results_2D", dpi=300)
#plt.show()
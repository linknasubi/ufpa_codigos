import statistics as st
import matplotlib.pyplot as plt
import math
from statistics import NormalDist



array = [64,  67,  94,  89, 119,  70,  81, 104,  89,  61,  93,  79,  84,
76,  58,  84,  99,  83, 111,  87,  72, 104,  55,  76, 102, 100,
88,  86,  75,  89,  92,  67,  99,  86, 116,  60,  46, 110, 104,
87, 104,  68,  88,  94,  48,  99,  91,  88,  99,  57,  78,  65,
74,  82,  79, 115,  71,  54, 114,  93,  96,  60, 111, 104, 114,
78, 127,  60,  82, 131,  71, 111, 101, 120,  91,  84,  80, 113,
87, 104,  81, 134,  71, 112,  74,  66,  69,  83,  90,  79,  98,
88, 124,  47,  97, 108,  78, 104,  49, 122, 101,  91,  75,  45,
91,  89,  88,  78,  84, 102,  72,  78,  92, 116,  79, 103,  65,
101,  29,  87,  71, 127,    94,  79,  80,  75,  74,  88,  27,
50,  86,  87,  77, 114, 95,  77,  87,  96, 101,  78, 105,  58,
70,  70,  99,  62,  81,  93,  87,  87,  90,  87,  82, 117,  68,
72, 118,  95, 127, 106,  88,  81, 109, 104, 108, 114,  96,  94,
111,  69, 108, 101,  55,  92,  89,  84,  38,  54,  55,  79,  77,
127,  79,  49,  62, 104,  88,  59,  84, 126,  54, 101,  79,  79,
100,  89, 100,  70,  85, 54]


# array = [11,  5,  2,  0,  9,  9,  1,  5,  1,  3,
# 3,  3,  7,  4,  12,  8,  5,  2,  6,  1,
# 11,  1,  2,  4,  2,  1,  3,  9,  0,  10,
# 3,  3,  1,  5,  18,  4,  22,  8,  3,  0,
# 8,  9,  2,  3,  12,  1,  3,  1,  7,  5,
# 14,  7,  7,  28,  1,  3,  2,  11,  13,  2,
# 0,  1,  6,  12,  15,  0,  6,  7,  19,  1,
# 1,  9,  1,  5,  3,  17,  10,  15,  43,  2,
# 6,  1,  13,  13,  19,  10, 9,  20,  19,  2,
# 27,  5,  20,  5,  10,  8,  2,  3,  1,  1,
# 4,  3,  6,  13,  10,  9,  1,  1,  3,  9,
# 9,  4,  0,  3,  6,  3,  27,  3,  18,  4,
# 6,  0,  2,  2,  8,  4,  5,  1,  4,  18,
# 1,  0,  16,  20,  2,  2,  2,  12,  28,  0,
# 7,  3,  18,  12,  3,  2,  8,  3,  19,  12,
# 5,  4,  6,  0,  5,  0,  3,  7,  0,  8,
# 8,  12,  3,  7,  1,  3,  1,  3,  2,  5,
# 4,  9,  4,  12,  4,  11,  9,  2,  0,  5,
# 8,  24,  1,  5,  12,  9,  17,  12,  6,
# 4,  3,  5,  7,  4,  4,  4,  11,  3,  8
# ]




media = st.mean(array)
mediana = st.median(array)
moda = st.mode(array)
minim = min(array)
maxim = max(array)
quartil = st.quantiles(array)

amplit = maxim - minim
DP = st.stdev(array)
varian = st.variance(array)
var_co = (DP/media) * 100


def outlierFinder(array):
    A = quartil[2] - quartil[0]
    mod_outlier = []
    ext_outlier = []
    
    for i in array:
        if i < (quartil[0] - 1.5*A) or i>(quartil[2] + 1.5*A):
            mod_outlier.append(i)
        
        if i < (quartil[0] - 3*A) or i>(quartil[2] + 3*A):
            ext_outlier.append(i)
    
    return mod_outlier, ext_outlier

outliers = outlierFinder(array)



def corrAnalysis(array):
    x = []
    y = []
    
    for i in range(0, len(array)-1, 2):
        x.append(array[i])
    
    for i in range(1, len(array), 2):
        y.append(array[i])
    
    return x, y

x,y = corrAnalysis(array)
plt.plot(x, y, 'o')
plt.show()


K_classes = round(1 + (3.3*math.log10(len(array))))
class_step = round(amplit/K_classes, 2)


def histogramMaker(array, k_classes, class_step):
    histogram = []
    frequency = 0
    
    for i in range(k_classes):
        frequency = 0
        for j in range(len(array)):
            if array[j] >= i*class_step and array[j] <= (i+1)*class_step:
                frequency += 1
                
        histogram.append(frequency)
    
    
    return histogram
        

histograma = histogramMaker(array, K_classes, class_step)


    

plt.hist(array, bins=K_classes)
plt.show()



def distrNormal(array):
    val_array = []


    
    for i in set(array):
        
        #val_array.append( (1/(DP) )*math.exp( (- i - media)**(2)/(2*varian))  )
        #val_array.append(round(1 - math.exp((-inv_media*i)), 2))
        val_array.append( NormalDist(mu=media, sigma=DP).cdf(i) )


        
    return val_array


def aderTeste(array):
    
    aux = 0
    
    freq = [array.count(x) for x in set(array)]
    freq_ac = []
    freq_ac_norm = []
    
    for i in (set(array)):
        aux+= array.count(i)
        freq_ac.append(aux)
        freq_ac_norm.append(round(aux/len(array), 2))
    
    
    
    freq_esp = distrNormal(array)
    
    D = []
    
    for i in range(len(freq_ac_norm)):
        D.append(round(abs(freq_esp[i] - freq_ac_norm[i]), 2))
    
    aderente = 1.36/(len(array)**(1/2)) > max(D)
    
    array.sort()
    array = list(set(array))
    
    

    
    return freq, freq_ac, freq_ac_norm, freq_esp, D, aderente
    
    

aderencia = aderTeste((array))
















import random


array = []
frequency = []

for i in range(0,100):

    array.append(random.randint(1,10))


for i in range(1, 11):
    frequency.append(array.count(i))
    print('Frequência do número ' + str(i)+' - '+ str(frequency[i-1]))




def evenProb():
    value = 0
    for i in range(2, 10, 2):
        value += frequency[i]
        
    print(str(value)+"/"+str(100))
    
evenProb()


def primeProb():
    value = 0
    
    for i in range(2, 8):
        if i == 2 or i == 3 or i == 5 or i == 7:
            value += frequency[i]
            
    print(str(value)+"/"+str(100))
        


primeProb()



def less5Prob():
    value = 0
    
    for i in range(1, 5):
        value += frequency[i]
        
    print(str(value)+"/"+str(100))


less5Prob()



def even3Prob():
    value = 0
    
    for i in range(4, 10, 2):
        value += frequency[i]
        
    print(str(value) + "/" + str(100))



even3Prob()










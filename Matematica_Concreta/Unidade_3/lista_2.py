import random

import pandas as pd

array = []
frequency = []

for i in range(0,100):

    array.append(random.randint(1,10))


for i in range(1, 11):
    frequency.append(array.count(i))

import pandas as pd
import numpy as np

da1 = 'shall see sun soon'
da2 = 'we shall see sun shine soon'

db1 = 'your mother drives you in the car'
db2 = 'in mother russia car drives you'

def get_shingle(size,f):
    #shingles = set()
    # print(f)
    for i in range (0,len(f)-size+1):
        yield tuple(f[i:i+size])


def jaccardCoefficient(shingle1, shingle2):

    jc = len(shingle1 & shingle2) / len(shingle1 | shingle2)

    print(round(jc,1))

# For 2 shingles part
shinglesa1 = { i for i in get_shingle(2,da1.split())}
shinglesa2 = {i for i in get_shingle(2, da2.split())}
# shinglesb1 = {i for i in get_shingle(2, db1.split())}
# shinglesb2 = {i for i in get_shingle(2, db2.split())}

# print(shinglesa1)
# print(shinglesa2)
Similarity1 = jaccardCoefficient(shinglesa1, shinglesa2)

# Similarity2 = jaccardCoefficient(shinglesb1, shinglesb2)

# for 3-Shignles part
# shinglesa11 = { i for i in get_shingle(3,da1.split())}
# shinglesa21 = { i for i in get_shingle(3,da2.split())}
# shinglesb11 = { i for i in get_shingle(3,db1.split())}
# shinglesb21 = { i for i in get_shingle(3,db2.split())}

# Similarity11 = jaccardCoefficient(shinglesa11,shinglesa21)
# Similarity21 = jaccardCoefficient(shinglesb11,shinglesb21)
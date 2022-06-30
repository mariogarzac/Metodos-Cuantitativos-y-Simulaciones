#!/usr/bin/python3

import math
import matplotlib.pyplot as plt

# Pide input de archivo y cantida de decimales
fileName = input("Nombre del archivo: ")
d = int(input("Numero de decimales a truncar: "))
N = 0
array = []


# Lee el archivo y agreaga todos los elementos a un arreglo
with open(fileName, "r") as arch:
        while (line := arch.readline()):
            N += 1
            array.append(round(float(line.strip('\n')),d))

maxNum = round(max(array), d)
minNum = round(min(array), d)
array.sort()

# Calcula C y W
C = math.ceil(1 + (3.3 * math.log(N,10)))
W = round((maxNum - minNum)/C , d)

# Inicializa los arreglos que contienen los rangos y las frecuencias
rangeTable = [0 for _ in range(C + 1)]
freqTable = [0 for _ in range(C)]

# Calcula los rangos del histograma
for i in range(1, C):
    rangeTable[i] = round(rangeTable[i - 1] + W, d)

rangeTable[0] = minNum
rangeTable[C] = maxNum + (1/10 ** d)

# Se cuenta la frecuencia de los elementos en los rangos 
j = 1
for i in range(N):
    if (array[i] < rangeTable[j]):
        freqTable[j - 1] += 1
    else:
        j += 1
        if (j <= C):
            freqTable[j - 1] += 1
        
# Prints 
print("N: {}".format(N))
print("C: {}".format(C))
print("Max: {} Min: {}".format(maxNum, minNum))
print("W: {}".format(W))
print(len(freqTable))
print(len(rangeTable))

ranges = []
for i in range(0, C):
    ranges.append("[{}, {})".format(rangeTable[i], rangeTable[i + 1]))
    print("[{}, {}) {}".format(rangeTable[i], rangeTable[i + 1], freqTable[i]))

print("Sum of frequencies: {}".format(sum(freqTable)))

# Plotting 
plt.rc('xtick', labelsize=7)    
plt.rc('ytick', labelsize=9)    
plt.title("Frequencies of Grouped Data")

plt.bar(ranges,freqTable)
plt.show()


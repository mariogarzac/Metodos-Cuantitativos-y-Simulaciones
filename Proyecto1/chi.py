#!/usr/bin/python3

# Mario Garza Chapa
# Juan Pablo González
# Michel Antoine Dionne

def getSeed(x, a, c, m, og, index):
    if (index == numbersGenerated):
        return 0
    else:
        results[index] = (round(x / m, 4))
        index += 1
        x = ((a * x) + c) % m
        getSeed(x, a, c, m, og, index)

def chiSquaredTest():
    # Variable declaration
    x = int(input("Escribe la semilla: "))
    a = int(input("Escribe la a: "))
    c = int(input("Escribe la c: "))
    m = int(input("Escribe la m: "))
    global numbersGenerated; numbersGenerated = int(input("Cantidad de números que se generarán: "))
    global results; results = [0 for _ in range(numbersGenerated)]

    chiFile = input("Nombre del archivo para chi: ")
    originalSeed = x
    N = 0
    data = []
    expected = 0

    # Array declaration
    ranges = [0.0000,0.1000,0.2000,0.3000,0.4000,0.5000,0.6000,0.7000,0.8000,0.9000,1.0000]
    observed = [0 for _ in range(10)]
    arrExpected = [0 for _ in range(10)]    

    # Lee el archivo y agreaga todos los elementos a un arreglo
    with open(chiFile, "r") as arch:
            while (line := arch.readline()):
                N += 1
                data.append(round(float(line.strip('\n')),5))
    
    expected = N / 10
    data.sort()

    # Gets frist results and appends to results array 
    x = ((a * x) + c) % m
    results.append(round(x / m ,4))
    # Gets rest of results
    getSeed(x, a, c, m, originalSeed, 0)

    # Creates observed table
    j = 1
    i = 0
    while (i < N):
        if (data[i] < ranges[j]):
            observed[j - 1] += 1
            i += 1
        else:
            j+= 1

    # Fills expected array
    for i in range(10):
        arrExpected[i] = round(((observed[i] - expected) ** 2)/expected,4)

    # Prints
    print("Xo: ", originalSeed)
    print("a:  ", a)
    print("c:  ", c)
    print("m:  ", m)
    print("N:  ", N)
    print("Results:", results, '\n')

    expectedSum = sum(arrExpected)
    print("Intervals  Observed (O - E)^2 / E")
    for i in range(10):
        print("[{}, {}) {}        {}".format(ranges[i], ranges[i + 1], observed[i], arrExpected[i]))
    print("------------------- x^2: {}".format(expectedSum))

    print("H0: Generated numbers are not different from the uniform distribution.")
    print("H1: Generated numbers are different from the uniform distribution. ")
    
    if (expectedSum > 16.91):
        print("Since {} > 16.91, H0 is rejected.\n".format(expectedSum))
    else: 
        print("Since {} < 16.91, H0 is not rejected.\n".format(expectedSum))
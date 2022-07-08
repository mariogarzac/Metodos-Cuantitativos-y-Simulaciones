#!/usr/bin/python3

# Mario Garza Chapa
# Juan Pablo González
# Michel Antoine Dionne

import math

def runsTest():
    #Extraemos la información del archivo
    runsValues = []
    entrada = input("Por favor ingrese el nombre del archivo: ")
    with open(entrada, "r") as arch:
        for line in arch.readlines():
            runsValues.append(round(float(line.strip('\n')),5))

    #Cuenta los signos entre cada uno
    signHolder = []
    for i in range(0,len(runsValues)-1):
        if runsValues[i+1] >= runsValues[i]:
            signHolder.append('+')
        elif runsValues[i+1] < runsValues[i]:
            signHolder.append('-')

    #Cuenta las rachas a partir de los signos
    rachasCounter = 1
    for i in range(0,len(signHolder)-1):
        if signHolder[i] != signHolder[i+1]:
            rachasCounter += 1

    #Calculamos los valores para rechazar o no rechazar la hipotesis
    uR = round(((len(signHolder) * 2) - 1)/3,5)
    oR = round(((len(signHolder) * 16) - 29)/90,5)
    o = round(math.sqrt(oR),5)
    zR = round((rachasCounter-uR) / o,5)

    #Revisamos si se rechaza o no se rechaza la hipotesis al igual que imprimimos todos los datos
    # print("\nTenemos los signos generados: ",signHolder)
    # print("Con una cantidad de rachas calculadas de: {}".format(rachasCounter))
    # print("El parametro de Miu dio: {}".format(uR))
    # print("El parametro de Sigma dio: {}".format(o))
    # print("El parametro de Zscore dio: {}".format(zR))
    # print("H0: la aparición de los números es aleatoria")
    # if abs(zR) > 1.96:
    #     print("Se rechaza la Ho porque el valor de |{}| es mayor a 1.96".format(zR))
    # else:
    #     print("No se rechaza la Ho porque el valor de |{}| es menor a 1.96".format(zR))

    print("Genrated signs: ")
    for i in range(len(signHolder)):
        print("{} ".format(signHolder[i]), end = '')
    print("\n")
    print("Total: ", len(signHolder))
    print("Total runs: ", rachasCounter)
    print("Statistics\n")
    print("Miu = ", uR)
    print("Sigma = ", o)
    print("Zscore = ", zR)

    print("H0: Apperance of the numbers is random.")
    print("H1: Apperance of the numbers is not random.\n")

    if abs(zR) > 1.96:
        print("Since |{}| > 1.96, H0 is  rejected.".format(zR))
    else:
        print("Since |{}| < 1.96, H0 is not rejected".format(zR))




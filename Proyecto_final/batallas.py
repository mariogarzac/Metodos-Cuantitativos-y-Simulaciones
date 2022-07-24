import random

def writeMatrix(file, matrix):
    txt = "\t"
    for i in range(0,len(matrix)):
        txt+=str(i+1)+"\t"
    txt+="\n"
    file.write(txt)
    for i in range(0,len(matrix)):
        mat = str(i+1)
        for j in range(0,len(matrix)):
            mat += "\t"+str(matrix[i][j])
        mat += "\n"
        file.write(mat)
    file.write("\n")

def countFaction(warriors):
    fact = 0
    for i in range(0,len(warriors)):
        if warriors[i] != 0:
            fact+=1
    return fact

def writeWarriors(file, warriors):
    file.write("El numero de guerreros de cada faccion es:\n")
    for i in range(0,len(warriors)):
        # if warriors[i] == 0:
        #     pass
        # else:
        file.write("La faccion {} tiene {} guerreros\n".format(i+1,warriors[i]))
    file.write("\n")

def createMatrix(n):
    if n == 2:
        return [[0,1],[1,0]]
    else:
        matrix = []
        for i in range(n):
            group = [round(random.random(),2) for i in range(n)]
            for j in range(n):
                if j == i:
                    group[j] = 0
            s = sum(group)
            group = [ round(i/s,2) for i in group]
            matrix.append(group)
        return matrix

def checkWarriors(warriors, factions, matrix, file):
    for i in range(len(warriors)-1,-1,-1):
        if warriors[i] == 0:
            file.write("Han eliminado a la faccion {}\n\n".format(factions[i]))
            warriors.pop(i)
            factions.pop(i)
            if len(warriors) >= 2:
                matrix = createMatrix(len(warriors))
                file.write("Cambio la matriz\n")
                writeMatrix(file,matrix)
    return warriors, factions, matrix

def main():
    #n = int(input("Ingrese el numero de facciones: "))
    newFile = open("battle.txt","w")
    matrix = createMatrix(3)
    writeMatrix(newFile, matrix)
    warriors = [(random.randint(1,10)*10) for i in range(3)]
    factions = [str(i+1) for i in range(3)]
    writeWarriors(newFile, warriors)

    while countFaction(warriors) > 1:
        #Condición para ver si ya eliminaron a alguien
        warriors, factions, matrix = checkWarriors(warriors, factions, matrix, newFile)
        if len(warriors) == 1:
            break
        else:
            #Los ataques
            battle = random.sample(factions,2)
            newFile.write("La faccion {} ataca a la faccion {}\n".format(battle[0],battle[1]))

            # if warriors[int(battle[1])-1] - 10 == 0:
            #     warriors[int(battle[1])-1] -= 10
            # else:
            #     warriors[int(battle[1])-1] -= 10
            #     writeWarriors(newFile, warriors)
            warriors[int(battle[1])-1] -= 10
            writeWarriors(newFile, warriors)
    
    warriors, factions, matrix = checkWarriors(warriors, factions, matrix, newFile)
    newFile.write("La faccion ganadora es la {}".format(factions[0]))
    

if '__main__' == __name__:
    main()
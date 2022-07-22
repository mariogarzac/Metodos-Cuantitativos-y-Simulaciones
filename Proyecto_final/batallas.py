import random

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

def main():
    a = createMatrix(3)
    #print(a)
    #Poner cantidad de guerreros
    #Un for para hacer los ataques
    #Cada que se elimine un grupo, llamar a create matrix
    

if '__main__' == __name__:
    main()
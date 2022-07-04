# Mario Garza Chapa
# Juan Pablo González
# Michel Antoine Dionne

#Tomamos los valores entrados por el usuario
def runTests():
    x0 = int(input("Por favor ingrese el valor de x0: "))
    a = int(input("Por favor ingrese el valor de a: "))
    c = int(input("Por favor ingrese el valor de c: "))
    m = int(input("Por favor ingrese el valor de m: "))
    numNumber = int(input("Ingrese el número de números a generar: "))
    valueHolder = []

    # calculamos nuestros números "aleatorios"
    counter = 0
    while counter < numNumber:
        val = ((a*x0) + c) % m
        valueHolder.append(round(val,4)/m)
        x0 = round(val,4)
        counter += 1
    print("Los números generados fueron: ",valueHolder,"\n")
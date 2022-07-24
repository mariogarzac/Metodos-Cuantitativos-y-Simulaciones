import random

def setTime(minutos : int):
    if (minutos < 10):
        return "0" + str(minutos)
    else:
        return str(minutos)

def fila(N,tLlegarMax, tCajeroMax):
    salida = open("fila.txt","w")
    hora, minutos = 9,0
    tiemposTramite = [random.randint(1,tCajeroMax) for i in range(N)]
    tiempoLlegadas = [random.randint(1,tLlegarMax) for i in range(N)]
    previo, llegada, inicio, espera, inactividad, esperando = 0, 0, 0, 0, 0, 0
    horaLlegada = 9

    #Añadir el primer visitante manualmente
    salida.write("cliente | tiempo entre llegadas |   Hora de llegada  |  Tiempo del tramite  |    Inicio de Servicio    | Termina servicio  | Tiempo de espera cliente\n")
    llegaPrimero = random.randint(1,tCajeroMax)
    tiempoServicio = llegaPrimero
    counter = 1
    salida.write("{:5.0f}   |   {:15.0f}     |   {:11.0f}:{}   |   {:17.0f}  |   {:17.0f}:{}   |   {:8.0f}:{}     |           0\n"
        .format(counter,0,  hora, setTime(minutos),   llegaPrimero,  hora, setTime(minutos),  hora, setTime(minutos + llegaPrimero)))
    minutos+=llegaPrimero
    previo = minutos
    inicio = minutos

    #Todos los demás
    while counter < N:
        #Control de la hora de salida
        horaFinal = hora
    
        llegada += tiempoLlegadas[counter]
        #Verificar horas
        if llegada >= 60:
            llegada -= 60
            horaLlegada += 1

        #Verificar disponibilidad
        if previo >= llegada:
            inicio = previo
            esperando += 1
        else:
            inicio = llegada
            inactividad += (llegada - previo)
    
    
        # El tiempo de espera de los clientes
        if inicio > llegada:
            espera += (inicio - llegada)
        tiempoServicio += tiemposTramite[counter]

        #La hora de salida
        total = inicio+tiemposTramite[counter]
        if total >= 60:
            total-=60
            horaFinal+=1
        #Imprimir el formato
        salida.write("{:5.0f}   |   {:15.0f}     |   {:11.0f}:{}   |   {:17.0f}  |   {:17.0f}:{}   |   {:8.0f}:{}     |    {:8d} \n".format(counter+1
        ,tiempoLlegadas[counter],
        horaLlegada, setTime(llegada),
        tiemposTramite[counter],
        hora,setTime(inicio),
        horaFinal, setTime(total) 
        ,inicio - llegada ))
        
        #Suma a los iteradores
        if inicio + tiemposTramite[counter] >= 60:
            inicio = inicio + tiemposTramite[counter] -60
            hora+=1
        else:
            inicio += tiemposTramite[counter]
        previo = inicio
        counter+=1

    salida.write('\n')
    salida.write("Tiempo esperado por cliente: {} minutos\n".format(espera/counter))
    salida.write("Probabilidad de tiempo de que un cliente espere en la fila: {}%\n".format((esperando/counter) * 100))
    salida.write("Porcentaje de tiempo que estuvo inactivo el ATM: {}%\n".format((inactividad/(tiempoServicio + inactividad) * 100)))
    salida.write("Tiempo promedio de servicio: {} minutos".format(tiempoServicio/counter))
    salida.close()

def main():
    numClientes = int(input("Por favor ingresa el número de clientes a usar el ATM "))
    tiempoLlegada = int(input("Por favor ingresa el número de minutos máximo que tardará un cliente "))
    tiempoTramite = int(input("Por favor ingresa el número de minutos máximo que tomará un cleinte "))
    fila(numClientes,tiempoLlegada,tiempoTramite)

if '__main__' == __name__:
    main()
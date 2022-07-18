import random

def fila(N,tLlegarMax, tCajeroMax):
    hora, minutos = 9,0
    tiemposTramite = [random.randint(1,tCajeroMax) for i in range(N)]
    tiempoLlegadas = [random.randint(1,tLlegarMax) for i in range(N)]
    previo, llegada, inicio, espera, inactividad, esperando = 0, 0, 0, 0, 0, 0

    #Añadir el primer visitante manualmente
    print("cliente | tiempo entre llegadas | Hora de llegada | tiempo del tramite | inicio de servicio | Termina servicio")
    llegaPrimero = random.randint(1,tCajeroMax)
    counter = 1
    print("{}   |   {}  |   {}:{}   |   {}  |   {}:{}   |   {}:{}"
        .format(counter,0,  hora, minutos,   llegaPrimero,  hora, minutos,  hora, minutos+llegaPrimero))
    minutos+=llegaPrimero
    previo = minutos
    inicio = minutos

    #Todos los demás
    while counter < N:

        #Suma para las horas
        if (minutos + tiemposTramite[counter]) >= 60:
            minutos = minutos + tiemposTramite[counter] - 60
            hora += 1
    
        #Verificar disponibilidad
        llegada += tiempoLlegadas[counter]
        if previo >= llegada:
            inicio = previo
            esperando += 1
        else:
            inicio = llegada
            inactividad += (llegada - previo)
    
        # El tiempo de espera de los clientes
        if inicio > llegada:
            espera += (inicio - llegada)

        #Imprimir el formato
        print("{}     |{}     |{}:{}    |   {}  |   {}:{}   |   {}:{}".format(counter+1
        ,tiempoLlegadas[counter],
        hora, llegada,
        tiemposTramite[counter],
        hora,inicio,
        hora, inicio+tiemposTramite[counter]))

        #Suma a los iteradores
        inicio+=tiemposTramite[counter]
        previo = inicio
        counter+=1
    print('\nLa espera total fue de: ',espera)
    print('La inactividad total fue de: ',inactividad)
    print('El total de clientes esperando fue de: ',esperando)


def main():
    fila(4,5,5)

if '__main__' == __name__:
    main()
import random

def setTime(minutos : int):
    if (minutos < 10):
        return "0" + str(minutos)
    else:
        return str(minutos)

def fila(N,tLlegarMax, tCajeroMax):
    hora, minutos = 9,0
    tiemposTramite = [random.randint(1,tCajeroMax) for i in range(N)]
    tiempoLlegadas = [random.randint(1,tLlegarMax) for i in range(N)]
    previo, llegada, inicio, espera, inactividad, esperando = 0, 0, 0, 0, 0, 0

    #Añadir el primer visitante manualmente
    print("cliente | tiempo entre llegadas |   Hora de llegada  |  Tiempo del tramite  |    Inicio de Servicio    | Termina servicio  | Tiempo de espera cliente")
    llegaPrimero = random.randint(1,tCajeroMax)
    tiempoServicio = llegaPrimero
    counter = 1
    print("{:5.0f}   |   {:15.0f}     |   {:11.0f}:{}   |   {:17.0f}  |   {:17.0f}:{}   |   {:8.0f}:{}     |           0"
        .format(counter,0,  hora, setTime(minutos),   llegaPrimero,  hora, setTime(minutos),  hora, setTime(minutos + llegaPrimero)))
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
        tiempoServicio += tiemposTramite[counter]

        #Imprimir el formato
        print("{:5.0f}   |   {:15.0f}     |   {:11.0f}:{}   |   {:17.0f}  |   {:17.0f}:{}   |   {:8.0f}:{}     |    {:8d} ".format(counter+1
        ,tiempoLlegadas[counter],
        hora, setTime(llegada),
        tiemposTramite[counter],
        hora,setTime(inicio),
        hora, setTime(inicio+tiemposTramite[counter]) 
        ,inicio - llegada ))
        
        #Suma a los iteradores
        inicio+=tiemposTramite[counter]
        previo = inicio
        counter+=1
    
    print('\n')
    print('La espera total fue de: ',espera)
    print('La inactividad total fue de: ',inactividad)
    print('El total de clientes esperando fue de: ',esperando)

    print('\n')
    print("Tiempo esperado por cliente: ", espera/counter)
    print("Probabilidad de tiempo de que un cliente espere en la fila: ", (esperando/counter) * 100)
    print("Porcentaje de tiempo que estuvo inactivo el ATM : ", inactividad/(tiempoServicio + inactividad) * 100)
    print("Tiempo promedio de servicio: ", tiempoServicio/counter)
def main():
    fila(4,5,5)

if '__main__' == __name__:
    main()
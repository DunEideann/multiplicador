# Este script resuelve el siguiente problema:
# 3 hermanos deben viajar a visitar a su tío que vive a 300 kilómetros de distancia.
# Tienen una motocicleta que puede llevar hasta dos personas a la vez,
#  y viaja a una velocidad d e 60 km/hr y cada persona puede caminar a una velocidad de 15 km/hr.
# Si todos empiezan desde su hogar al mismo tiempo,<br>
# ¿Cuál es el tiempo más corto posible en que los 3 alcancen su destino?.



distancia = 300 #en kilometros
bikeSpeed = 60  # en kilometros por hora
personSpeed = 15 # en kilometros por hora
persona1 = 0
persona2 = 0
persona3 = 0
totalTime = 0.000
deltaTime = 1/3600 # corresponde a 1 minuto, puede ser cualquiera, dado que es los espacios de integracion que se usaran solamente.
count = 0 # personas que han llegado
persona2Reversa = False
persona3InBike = False
forma = input("""
Eliga una de las dos formas: 
    1 : Llega a persona y vuelve a buscar al segundo que estaba caminando.
    2 : Si elige forma 2 debe elegir el numero de iteraciones, siento 1 el minimo y 1800 el maximo (ideal 180).
>   """)


if forma == "1":

    # Forma 1 
    while(count < 3):
        if persona1>=distancia:
            count = 1
            persona2Reversa = True
        else:
            persona1 += bikeSpeed*deltaTime

        if persona2Reversa:
            persona2 -= bikeSpeed*deltaTime
        else :
            persona2 += bikeSpeed*deltaTime


        if persona2<=persona3:
            persona3InBike = True
            perona2Reversa = False

        if persona3InBike:
            persona3 += bikeSpeed*deltaTime
            if persona3>=distancia:
                count += 2
        else :
            persona3 += personSpeed*deltaTime

        totalTime += deltaTime

    else:
        print(f"Llegaron los 3 en un tiempo: {totalTime}")

if forma == "2":
    iteraciones = int(input("> "))
    distanciaIterada = distancia/iteraciones
    numIteracion = 1

    persona1NotArrive = True
    persona2NotArrive = True
    persona3NotArrive = True
    llevandoPersona3 = False
    # Forma 2

    # Aca empiezo el ciclo
    while(count < 3):
        # Llevando persona 1
        if llevandoPersona3==False:

            if persona1 >= distanciaIterada*numIteracion:
                llevandoPersona3 = True

            persona1 += bikeSpeed*deltaTime
            persona2 += bikeSpeed*deltaTime
            persona3 += personSpeed*deltaTime

        # Llevando persona 3
        elif llevandoPersona3:

            if persona2<=persona3:
                persona3InBike = True
            if persona3 >= persona1:
                llevandoPersona3 = False
                numIteracion += 1
                persona3InBike = False


            if persona3InBike:
                persona2 += bikeSpeed*deltaTime
                persona3 += bikeSpeed*deltaTime
            else:
                persona2 -= bikeSpeed*deltaTime
                persona3 += personSpeed*deltaTime
            
            persona1 += personSpeed*deltaTime


        #Se cuenta tiempo transcurrido
        totalTime += deltaTime
        # Cuenta si llegaron las personas
        if persona1>=distancia and persona1NotArrive :
            count += 1
            persona1NotArrive = False

        if persona2>=distancia and persona2NotArrive :
            count += 1
            persona2NotArrive = False

        if persona3>=distancia and persona3NotArrive :
            count += 1
            persona3NotArrive = False
       

    else:
        print(f"Llegaron los 3 en un tiempo: {totalTime}")
        



    

def guardar_reserva(lista_de_reservas):
    print("Seleccionó Opción 1")
    cantidad_personas=int(input("Ingrese la cantidad de personas"))
    #validar la cantidad de personas que se pueden hospedar en habitación 
    #maximo 3 personas

    habitacion=int(input("Ingrese la habitación"))
    nombre_reserva=input("Ingrese el nombre de la reserva")
    precio=cantidad_personas*10000

    for n_persona in range(cantidad_personas):
        nombre_pasajero=input("Ingrese el nombre del pasajero")
        lista_de_reservas.append([habitacion,nombre_reserva,nombre_pasajero,precio])
    return lista_de_reservas
    

def buscar_reserva_por_habitacion(lista_de_reservas):
    print("Seleccionó la opción 2")
    habitacion_buscada=int(input("Ingrese numero de habitación"))
    largo_lista=len(lista_de_reservas)
    #imprimir toda la lista
    posicion_reserva_en_la_lista=-1
    mensaje="La habitación está vacía" 
    #recorrer toda la lista
    for fila in range(largo_lista):
        print("Impreso automaticamente",lista_de_reservas[fila])
        reserva_encontrada=lista_de_reservas[fila]
        numero_habitacion_encontrada=reserva_encontrada[0]
        
        if habitacion_buscada == numero_habitacion_encontrada:
            mensaje="Habitación reservada "
            posicion_reserva_en_la_lista=fila

    print(mensaje)
    return  posicion_reserva_en_la_lista

def mostrar_reserva(lista_de_reservas):
    print("Seleccionó la opción 3")
    habitacion_encontrada=buscar_reserva_por_habitacion(lista_de_reservas)
    #si encontré la habitación ocupada
    if habitacion_encontrada >= 0:
        print("La reserva es:",lista_de_reservas[habitacion_encontrada])
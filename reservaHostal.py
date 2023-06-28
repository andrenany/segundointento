from funciones import *

menu_activo = True
opcion_seleccionada = 0
lista_de_reservas=[
[100,"Juanito","Juan Soto", 18000],
[100,"Juanito","Josefa Mendez", 18000],
[200,"Aandrea","Andrea Gonzales", 12000],
[300,"Jose","José Oyarzún", 12000],
]

while menu_activo:
    print("Bienvenido al sistema del Fast Hotel")
    print("Seleccione una opción: ")
    print("1.- Guardar reserva")
    print("2.- Buscar reserva")
    print("3.- Mostrar reserva")
    print("4.- Modificar Reserva")
    opcion_seleccionada=int(input("Ingrese un número"))

    if opcion_seleccionada == 1:
        #se crea una nueva lista y se guardan los nuevos pasajeros
        reserva_modificada=guardar_reserva(lista_de_reservas)
        #se actualiza la lista original
        lista_de_reservas=reserva_modificada
        print("Reserva guardada con éxito")
    
    if opcion_seleccionada == 2:
        buscar_reserva_por_habitacion(lista_de_reservas)
    
    if opcion_seleccionada == 3:
        mostrar_reserva(lista_de_reservas)




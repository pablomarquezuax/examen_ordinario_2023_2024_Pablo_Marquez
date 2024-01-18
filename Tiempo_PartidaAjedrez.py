# Inicialización de variables
tiempo_carlsen = 180
tiempo_nakamura = 180
tiempo_movimiento = 10
turno = "Carlsen"

# Función para cambiar el tiempo de movimiento a 5 segundos cuando se alcance 1 minuto
def cambiar_tiempo_movimiento():
    global tiempo_movimiento
    if tiempo_carlsen < 60 or tiempo_nakamura < 60:
        tiempo_movimiento = 5

# Función para mostrar el tiempo actual y el turno del jugador
def mostrar_estado():
    print(f"Tiempo Carlsen: {tiempo_carlsen} segundos")
    print(f"Tiempo Nakamura: {tiempo_nakamura} segundos")
    print(f"Turno de {turno}")

# Juego de ajedrez
while True:
    mostrar_estado()
    
    # Verificar si un jugador ha perdido su tiempo o si el usuario quiere salir
    if tiempo_carlsen <= 0 or tiempo_nakamura <= 0:
        if tiempo_carlsen <= 0:
            print("¡Hikaru Nakamura gana!")
        else:
            print("¡Magnus Carlsen gana!")
        break
    
    movimiento = input(f"Ingrese el nombre del jugador para mover ({turno}): ")
    
    # Validar que el jugador ingresado coincida con el turno actual
    if movimiento != turno:
        print("¡No es el turno de ese jugador!")
        continue
    
    # Realizar el movimiento y actualizar el tiempo
    if turno == "Carlsen":
        tiempo_carlsen -= tiempo_movimiento
        turno = "Nakamura"
    else:
        tiempo_nakamura -= tiempo_movimiento
        turno = "Carlsen"
    
    # Cambiar el tiempo de movimiento si es necesario
    cambiar_tiempo_movimiento()

print("Fin del juego")

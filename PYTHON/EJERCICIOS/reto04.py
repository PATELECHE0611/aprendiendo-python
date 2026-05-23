# ============================================================
# RETO #4 — GESTOR DE ESTUDIANTES
# ============================================================
# Crea un programa con menu que permita:
# 1. Agregar estudiantes a una lista (el usuario decide cuantos)
# 2. Ver todos los estudiantes agregados enumerados
# 3. Salir del programa
# El programa debe seguir funcionando hasta que el usuario
# elija salir.
# ============================================================

menu = ""         # Variable inicial para arrancar el while
estudiantes = []  # Lista vacia donde guardaremos los nombres

while menu != "3" or menu != "salir":

    # Mostramos el menu
    print("MENU")
    print("1. Agregar estudiante")
    print("2. Ver todos los estudiantes")
    print("3. salir")

    menu = input("¿Que deseas?: ")

    # Opcion salir
    if menu == "3" or menu == "salir":
        print("has salido con exito")
        break

    # Opcion agregar estudiantes
    if menu == "1" or menu == "agregar estudiante":
        n = int(input("¿Cuantos estudiantes quiere agregar?: "))

        # El for repite la pregunta exactamente n veces
        for i in range(1, n + 1):
            # append() agrega cada nombre al final de la lista
            estudiantes.append(input(f"ingresa el nombre del estudiante {i}: ").lower())

    # Opcion ver estudiantes
    elif menu == "2" or menu == "ver todos los estudiantes":
        print("la lista de estudiantes es: ")

        # enumerate() nos da el indice y el valor al mismo tiempo
        # el parametro 1 hace que empiece a contar desde 1
        for indice, i in enumerate(estudiantes, 1):
            print(f'{indice}.{i}')
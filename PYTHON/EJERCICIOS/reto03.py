# ============================================================
# RETO #3 — CALCULADORA CON FUNCIONES Y BUCLE
# ============================================================
# Mejora la calculadora del reto anterior organizando cada
# operacion dentro de su propia funcion. El programa no
# debe cerrarse despues de cada operacion, sino mostrar
# el menu nuevamente hasta que el usuario elija salir.
# Debe aceptar tanto el nombre de la operacion como su numero.
# ============================================================

# --- DEFINICION DE FUNCIONES ---
# Cada funcion recibe dos numeros, calcula y devuelve el resultado

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def divison(a, b):
    resultado = a / b
    return resultado

# --- PROGRAMA PRINCIPAL ---

operacion = ""  # Variable inicial para que el while pueda arrancar

while operacion != "salir" or operacion != "5":

    # Mostramos el menu de opciones
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. salir")

    # .lower() convierte la entrada a minusculas
    operacion = input("¿Que operacion desea?: ").lower()

    # Verificamos si el usuario quiere salir
    if operacion == "salir" or operacion == "5":
        print("has salido de la calculadora")
        break

    # try/except protege el programa si el usuario ingresa letras en vez de numeros
    try:
        a = int(input("ingrese el valor del primer numero: "))
        b = int(input("ingrese el valor del segundo numero: "))
    except:
        print("algo salio mal")

    # Llamamos la funcion correcta segun la operacion elegida
    if operacion == 'suma' or operacion == "1":
        print(f'el resultado de la suma es: {suma(a, b)}')
    elif operacion == 'resta' or operacion == "2":
        print(f'el resultado de la resta es: {resta(a, b)}')
    elif operacion == 'multiplicacion' or operacion == "3":
        print(f'el resultado de la multiplicacion es: {multiplicacion(a, b)}')
    elif operacion == 'divison' or operacion == "4":
        print(f'el resultado de la divison es: {divison(a, b)}')
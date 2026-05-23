# ============================================================
# RETO #2 — CALCULADORA BASICA
# ============================================================
# Crea un programa que pida dos numeros al usuario y le
# pregunte que operacion desea realizar (suma, resta,
# multiplicacion o division). El programa debe mostrar
# el resultado de la operacion elegida.
# El programa debe funcionar sin importar si el usuario
# escribe en mayusculas o minusculas.
# ============================================================

# Pedimos los dos numeros al usuario
a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))

# .lower() convierte lo que escribe el usuario a minusculas
operacion = input("¿Que operacion desea? (suma,resta,multiplicacion o division): ").lower()

# Calculamos todas las operaciones
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Mostramos el resultado segun la operacion elegida
if operacion == 'suma':
    print(f'resultado: {suma}')
elif operacion == "resta":
    print(f'resultado: {resta}')
elif operacion == "multiplicacion":
    print(f'resultado: {multiplicacion}')
elif operacion == "division":
    print(f'resultado: {division}')
# ============================================================
# RETO #1 — TARJETA DE PRESENTACION
# ============================================================
# Crea un programa que le pregunte al usuario su nombre,
# edad y ciudad. Con esos datos, imprime un mensaje de
# presentacion. El programa debe calcular automaticamente
# cuantos años tendra el usuario en 10 años.
# ============================================================

# Pedimos los datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))  # int() convierte el texto a numero entero
ciudad = input("Ingrese la ciudad donde vive: ")

# Calculamos la edad futura
suma = edad + 10

# Mostramos el mensaje con f-string (combina texto y variables)
print(f'Hola, me llamo {nombre}. Tengo {edad} años y vivo en {ciudad}. En 10 años tendre {suma} años.')
import random
nuevo_juego=""
while nuevo_juego!="no":
    numero=random.randint(1,100)
    numero_a_adivinar=0
    intentos=0
    while numero_a_adivinar!=numero:
        numero_a_adivinar=int(input("ingrese el numero (1-100): "))
        intentos+=1
        if numero_a_adivinar==numero:
            print("¡FELICITACIONES! HAS ENCONTRADO EL NUMERO")
            break
        elif numero_a_adivinar<numero:
            print("EL NUMERO QUE BUSCAS ES MAYOR (1-100)")
        elif numero_a_adivinar>numero:
            print("EL NUMERO QUE BUSCAS ES MENOR (1-100)")
    print(f"EL NUMERO LO ENCONTRASTE EN EL INTENTO NUMERO: {intentos}")
    nuevo_juego=input("¿QUIERE JUGAR DE NUEVO?(SI/NO): ").lower()
    if nuevo_juego=="no":
        print("has salido con exito")
        break
    else:
        print("NUEVO JUEGO")

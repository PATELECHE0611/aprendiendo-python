import random
new_game=""
while new_game!="no":
    numero=random.randint(1,100)
    num1=0
    intentos=0
    while num1!=numero:
        num1=int(input("ingrese el numero (1-100): "))
        intentos+=1
        if num1==numero:
            print("¡FELICITACIONES! HAS ENCONTRADO EL NUMERO")
            break
        elif num1<numero:
            print("EL NUMERO QUE BUSCAS ES MAYOR (1-100)")
        elif num1>numero:
            print("EL NUMERO QUE BUSCAS ES MENOR (1-100)")
    print(f"EL NUMERO LO ENCONTRASTE EN EL INTENTO NUMERO: {intentos}")
    new_game=input("¿QUIERE JUGAR DE NUEVO?(SI/NO): ").lower()
    if new_game=="no":
        print("has salido con exito")
        break
    else:
        print("NUEVO JUEGO")

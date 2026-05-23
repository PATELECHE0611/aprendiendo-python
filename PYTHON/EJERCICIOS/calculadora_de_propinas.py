print("BIENVENIDOS AL RESTAURANTE PATELECHE")
print("¿Cuantas personas van a comer?")
personas=[]
n_personas=(int(input('ingrese el numero de personas: ')))
def cuenta():
    total=0
    for i in range(n_personas):
        consumo=int(input("ingrese el valor consumido: "))
        total=total+consumo
    return total

def propina(total):
    print("¿deseas incluir la propina?")
    print("1.si")
    print("2.no")
    propina=(input("ingresa si o no: "))
    if propina == "1" or propina == "si":
        valor_propina=(10/100)*total
        return valor_propina
    else:
        print("NO INCLUYE LA PROPINA")
        return 0
    

def pagar(total,valor_propina):
    pagar=total+valor_propina
    print(f"el valor total a pagar es de: {pagar}")
    return pagar
total = cuenta()
valor_propina = propina(total)
pagar(total, valor_propina)
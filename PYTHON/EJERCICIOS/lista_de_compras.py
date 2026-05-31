menu=""
while menu!="3" or menu!="salir":
    print("MENU")
    print("1. AGREGAR PRODUCTO")
    print("2. VER LISTA DE PRODUCTOS")
    print("3. SALIR")
    menu=(input("ELIGE UNA DE LAS OPCIONES \n¿CUAL DESEAS?: "))
    if menu=="1" or menu=="AGREGAR PRODUCTO":
        producto={}
        lista_productos = []
        producto.append(["nombre"]input("ingrese el nombre del producto: "))
        producto.append(["precio"]int(input("ingrese el precio del producto: ")))



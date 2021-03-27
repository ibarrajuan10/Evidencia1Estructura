ventas = {}
totalDeVenta = 0
diccionario_venta = {}

while True:
    print("\n------MENU------")
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3  Salir del programa")
    opcion = input("Ingrese una opcion: ")

    if opcion == '1':
        clave = input("\nDime un numero identificador para la venta ")
        if clave in ventas:
            print("\nEse identificador ya esta registrado, intenta con otro")
        else:
            ventas[clave] = []
            while True:
                desc_articulo = input("Dime la descripcion del articulo: ")
                piezas_vendidas = int(input("Dime la cantidad de piezas vendidas: "))
                precio_venta = float(input("Dime el precio de venta: "))
                monto_total = piezas_vendidas * precio_venta
                print("Su monto total a pagar es de $ ",monto_total)
                totalDeVenta = totalDeVenta + monto_total
                ventas[clave].append([desc_articulo, piezas_vendidas, precio_venta, monto_total])
                respuesta = input("\n¿Deseas capturar otro articulo? (1-Si / 0-No): ")
                if respuesta == '0':
                    print("El total de la venta fue de: $",totalDeVenta)
                    diccionario_venta[clave]=totalDeVenta
                    venta_total = 0
                    break

    elif opcion == '2':
        clave = input("\nDime el identificador de la venta que deseas consultar: ")
        if clave in ventas:
            print("la venta con esa llave es: ",clave)
            columnas = ["Descripción","Cantidad","Precio venta","Precio total"]
            for columna in range(4):
                print(columnas[columna],'\t',end="")
            print("\n")
            for articulo in ventas[clave]:
                for i in range(4):
                    print(articulo[i],"\t\t",end="")
                print("\n")
            print(f'El precio total de la venta es: {diccionario_venta[clave]}') 

        else:
            print("\nLo siento, ese identificador no fue capturado")
    elif opcion == '3':
        break
    else: 
        print("Has introducido una opcion invalida") 

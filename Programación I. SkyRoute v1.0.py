# SkyRoute - Sistema de gestion de pasajes
# Autores: Lautaro Molina-DNI: 45244425 / Silvera Julián Andrés-DNI: 34914614 /Sánchez Rocío Eliana-DNI: 38646124 .
  

print("Bienvenidos a SkyRoute - Sistema de gestion de pasajes")
clientes = []
destinos = []
ventas = []

opcion = 0
while opcion != 8:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Gestionar clientes.")
    print("2. Gestionar destinos.")
    print("3. Gestionar ventas.")
    print("4. Consultar ventas.")
    print("5. Boton de arrepentimiento.")
    print("6. Ver reporte general.")
    print("7. Acerca del sistema.")
    print("8. Salir.")

    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Por favor, ingrese un numero valido..")
        continue

    #Submenu Gestion de Clientes
    if opcion == 1:
        while True:
            print("\n--- GESTION DE CLIENTES ---")
            print("1. Ver clientes.")
            print("2. Agregar cliente.")
            print("3. Modificar cliente.")
            print("4. Eliminar cliente.")
            print("5. Volver al menu anterior.")

            try:
                opcion_cliente = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Por favor, ingrese un numero valido.")
                continue

            if opcion_cliente == 1:
                print("Se mostraron los clientes registrados.")
            elif opcion_cliente == 2:
                print("Usted ha ingresado a 'Agregar Cliente'")
                nombre = input("Ingrese su nombre: ")
                dni = input("Ingrese el dni: ")
                email = input("Ingrese el Correo Electronico: ")
                print("Cliente cargado con exito.")
            elif opcion_cliente == 3:
                print("Usted ha ingresado a 'Modificar cliente'")
            elif opcion_cliente == 4:
                print("Usted ha ingresado a 'Eliminar cliente'")
            elif opcion_cliente == 5:
                print("Volviendo al menu anterior...")
                break
            else:
                print("Opcion invalida.")
    #Submenu Gestion de Destinos
    elif opcion == 2:
        while True:
            print("\n--- GESTION DE DESTINOS ---")
            print("1. Ver destinos.")
            print("2. Agregar destino.")
            print("3. Modificar destino.")
            print("4. Eliminar destino.")
            print("5. Volver al menu anterior.")

            try:
                opcion_destino = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Por favor, ingrese un numero valido.")
                continue

            if opcion_destino == 1:
                print("Se mostraron los destinos disponibles.")
            elif opcion_destino == 2:
                print("Usted ha ingresado a 'Agregar nuevo destino'")
                ciudad = input("Ciudad: ")
                pais = input("Pais: ")
                try:
                    precio = float(input("Precio del pasaje: $"))
                except ValueError:
                    print("El precio debe ser numerico")
                    continue
                print(f"Destino {ciudad}, {pais} agregado con exito. Precio: ${precio}")
            elif opcion_destino == 3:
                print("Usted ha ingresado a 'Modificar destino'")
            elif opcion_destino == 4:
                print("Usted ha ingresado a 'Eliminar destino'")
            elif opcion_destino == 5:
                print("Volviendo al menu anterior...")
                break
            else:
                print("Opcion invalida.")
    #Submenu Gestion de Ventas
    elif opcion == 3:
        while True:
            print("\n--- GESTION DE VENTAS ---")
            print("1. Ver ventas.")
            print("2. Registrar nueva venta.")
            print("3. Volver al menu anterior.")

            try: 
                opcion_ventas= int(input("Seleccione una opcion: "))
            except ValueError:
                print("Por favor, ingrese un numero valido.")
                continue
            
            if opcion_ventas == 1:
                print("Mostrando todas las ventas registradas(Falta almacenamiento)")
              
            elif opcion_ventas == 2:
                cliente = input("Nombre del cliente: ")
                destino = input("Destino: ")
                try:
                  precio = float(input("Precio del pasaje: $"))
                except ValueError:
                  print("El precio debe ser un numero.")
                  continue
                print(f"Venta registrada con exito: {cliente} compro un pasaje a {destino} por ${precio}.")

            elif opcion_ventas == 3:
                print("Volviendo al menu anterior...")
                break
            else:
                print("Opcion no valida. Porfavor, intente nuevamente.")
    #Submenu Gestion de Ventas
    elif opcion == 4:
      while True:
          print("\n--- CONSULTAR VENTAS ---")
          print("1.Consultar por cliente.")
          print("2.Consultar por destino.")
          print("3.Consultar por precio.")
          print("4.Volver al menu anterior.")

          try:
             opcion_consulta = int(input("Selecciona una opcion: "))
          except ValueError:
              print("Debe ingresar un valor valido.")
              continue

          if opcion_consulta == 1:
              print("Usted ha ingreado a 'Consultar por cliente.'")
              cliente = input("Ingrese el nombre del cliente: ")
              print(f"Mostando ventas realizadas por el cliente: {cliente} (Falta implementar)")
          
          elif opcion_consulta == 2:
              print("Usted ha ingreado a 'Consultar por destino.'")
              destino = input("Ingrese el nombre del destino a consultar:")
              print(f"Mostrando ventas al destino: {destino} (Falta implementar)")

          elif opcion_consulta == 3:
              print("Usted ha ingresado a 'Consultar por precio.'")
              try:
                precio_min = float(input("Precio minimo: $"))
                precio_max = float(input("Precio maximo: $"))
              except ValueError:
                print("Debe ingresar numeros validos para el precio.")
                continue
              print(f"Mostrando ventas entre ${precio_min} y ${precio_max}(Falta implementar)")

          elif opcion_consulta == 4:
              print("Volviendo al menu principal...")
              break
          else :
              print("Opcion no valida. Porfavor, intente nuevamente.")
    #Submenu Boton de arrepentimiento
    elif opcion == 5:
      while True:
        print("\n--- BOTON DE ARREPENTIMIENTO ---")
        print("1.Anular venta por DNI.")
        print("2.Anular venta por numero de ticket.")
        print("3.Volver al menu anterior.")

        try:
            opcion_arrepentimiento = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Debe ingresar un numero valido.")
            continue

        if opcion_arrepentimiento == 1:
            print("Usted ha ingresado a 'Anular venta por DNI")
            dni = int(input("Ingrese el DNI del cliente: "))
            print(f"Buscando y anulando venta asociada al DNI: {dni}(Falta implementar")

        elif opcion_arrepentimiento == 2:
            print ("Usted ha ingresado a 'Anular venta por numero de ticket'")
            num_ticket= int(input("Ingrese el numero de ticket: "))
            print (f"Anulando venta con numero de ticket: {num_ticket}")

        elif opcion_arrepentimiento == 3:
            print("Volviendo al menu anterior")
            break
        else:
          print("Opcion invalida. Porfavor, intente nuevamente.")
    #Submenu Reporte general
    elif opcion == 6:
       while True:
        print("\n--- REPORTE GENERAL ---")
        print("Clientes registrados: (Falta implementar)")
        print("Destinos cargados: (Falta implementar)")
        print("Ventas realizadas: (Falta implementar)")
        break
     #Submenu Acerca del sistema
    elif opcion == 7:
        print("\n--- ACERCA DEL SISTEMA ---")
        print("SkyRoute - Sistema de gestion de pasajes")
    elif opcion == 8:
        print("Muchas gracias por utilizar SkyRoute. ")
    else:
        print("Opcion invalida.")

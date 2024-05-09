pikachu = 4500
otaku = 5000
pulpo = 5200
anguila = 4800
menu_principal = True
menu_pedido = False
descuento = "soyotaku"
contPikachu = 0
contOtaku = 0
contPulpo = 0
contAnguila = 0
total_pikachu = 0
total_otaku = 0
total_pulpo = 0
total_anguila = 0


while True:
    if menu_principal:
        print("Menu principal\n")
        print("1. Ingresar pedido")
        print("2. Boleta")
        print("3. Salir")
        try:
            opc = int(input("Ingresar opcion del 1 al 3:\n"))
            if 1 <= opc <= 3:
                if opc == 1:
                    menu_principal = False
                    menu_pedido = True
                elif opc ==2:
                    print("Total\n")
                    print("Total")
                    print("Pikachu Roll", contPikachu, "\n")
                    print("Otaku Roll", contOtaku, "\n")
                    print("Pulpo Venenoso Roll", contPulpo, "\n")
                    print("Anguila anguila Roll", contAnguila, "\n")
                    subtotal = (total_pikachu + total_otaku + total_pulpo + total_anguila)
                    print("Subtotal: ", subtotal,"\n")
                    if codigo_descuento == descuento:
                        descuento_aplicado = subtotal * 0.1
                        total_con_descuento = subtotal - descuento_aplicado
                        print("Descuento aplicado: ", descuento_aplicado)
                        print("Total", total_con_descuento)
                elif opc == 3:
                    print("Estas saliendo de la aplicación")
                    break
        except ValueError as errorOpcion:
            print("Ingresa opción válida entre 1 y 3")       
    if menu_pedido:
        print("Menu pedido\n")
        print("1. Pikachu Roll")
        print("2. Otaku Roll")
        print("3. Pulpo Venenoso")
        print("4. Anguila Electrica Roll")
        print("5. Ingresar codigo de descuento")
        print("6. Volver")
        try:  
            opc_pedido = int((input("Ingresa opcion del 1 al 6:\n")))
            if 1<= opc_pedido <=6:
                if opc_pedido == 1:
                    while True:
                        numPikachu = int(input("Ingrese cantidad de rolls que desea llevar\n"))
                        if numPikachu > 0:
                            contPikachu += numPikachu
                            total_pikachu = contPikachu * pikachu
                            break
                        else:
                            print("Ingrese una cantidad válida mayor a 0")
                elif opc_pedido == 2:
                    while True:
                        numOtaku = int(input("Ingrese cantidad de rolls que desea llevar\n"))
                        if numOtaku > 0:
                            contOtaku += numOtaku
                            total_otaku = contOtaku * otaku
                            break
                        else:
                            print("Ingrese una cantidad válida mayor a 0")
                elif opc_pedido == 3:
                        while True:
                            numPulpo = int(input("Ingrese cantidad de rolls que desea llevar\n"))
                            if numPulpo > 0:
                                contPulpo += numPulpo
                                total_pulpo = contPulpo * pulpo
                                break
                            else:
                                print("Ingrese una cantidad válida mayor a 0")
                elif opc_pedido == 4:
                     while True:
                        numAnguila = int(input("Ingrese cantidad de rolls que desea llevar\n"))
                        if numAnguila > 0:
                            contAnguila += numAnguila
                            total_anguila = contAnguila * anguila
                            break
                        else:
                            print("Ingrese una cantidad válida mayor a 0")
                elif opc_pedido == 5:
                    print("Tiene codigo de descuento")
                    codigo_descuento = input("Ingrese codigo de descuento")
                    if codigo_descuento == descuento:
                        print("Descuento aplicado")
                    elif codigo_descuento != descuento:
                        print("Codigo incorrecto ingrese nuevamente")    
                elif opc_pedido == 6:
                    print("Estas saliendo del pedido")
                    menu_pedido = False
                    menu_principal = True                    
        except ValueError as errorOpcionPedido:
            print("Ingresa opcion valida entre el 1 y 6")
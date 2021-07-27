def clear():      #limpiar output
	import os
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def inicial():
    from links import busquedalinks
    busquedalinks()

def menu2():
    try: 
        clear()
        print("MENU DE OPCIONES")
        print("1. Redes sociales.")
        print("2. Imágenes.")
        print("3. Noticias")
        print("4. Eventos")
        print("5. Clima")
        print("6. Salir")
                
        op = input("Seleccione una opción a buscar: ")
        while(op == str() or op.isalpha() or op.isspace() or int(op) < 0 or int(op) > 6):
            op = input("Seleccione una opción a buscar: ")
        if(int(op) == 1):
            from RedesSociales import redessociales
            redessociales()
            input("Presione enter para continuar")
            menu2()
        elif (int(op) == 2):
            from Imagenes import descarga_imagenes
            from Imagenes import carpetafotos
            carpetafotos()
            input("Presione enter para continuar")
            menu2()
        elif(int(op) == 3):
            from Noticias import noticias
            from Noticias import excelnoti
            noticias()
            input("Presione enter para continuar")
            menu2()
        elif(int(op) == 4):
            from Fechas import linkseventos
            from Fechas import guardado
            linkseventos()
            input("Presione enter para continuar")
            menu2()
        elif(int(op) == 5):
            from Clima import lookingcity
            from Clima import clima
            lookingcity()
            menu2()
        elif(int(op) == 6):
            exit()
    except ValueError:
        clear()
        menu2()
        

def menu():
    try:
        clear()
        print("MENU DE OPCIONES")
        print("1. Redes sociales.")
        print("2. Imágenes.")
        print("3. Noticias")
        print("4. Eventos")
        print("5. Salir")
        
        op = (input("Seleccione una opción a buscar: "))
        while(op == str() or op.isalpha() or op.isspace() or int(op) < 1 or int(op) > 5):
            op = input("Seleccione una opción a buscar: ")
        if(int(op) == 1):
            from RedesSociales import redessociales
            redessociales()
            input("Presione enter para continuar")
            menu()
        elif (int(op) == 2):
            from Imagenes import descarga_imagenes
            from Imagenes import carpetafotos
            carpetafotos()
            input("Presione enter para continuar")
            menu()
        elif(int(op) == 3):
            from Noticias import noticias
            from Noticias import excelnoti
            noticias()
            input("Presione enter para continuar")
            menu()
        elif(int(op) == 4):
            from Fechas import linkseventos
            from Fechas import guardado
            linkseventos()
            input("Presione enter para continuar")
            menu2()
        elif(int(op) == 5):
            exit()

    except ValueError:
        clear()
        menu()
    
inicial()
menu()
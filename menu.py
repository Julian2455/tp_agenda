archivo=open("archivo.txt","r")
while True:
    print("Menu opciones: ")
    print("1--> Mostrar los nombres registrados")
    print("2--> Agregar un nuevo nombre a la lista")
    print("3--> Buscar un nombre en la lista")
    print("4--> SALIR")
    opcion=int(input("Ingrese la opcion: "))
    if opcion==1:
        archivo=open("archivo.txt","r")
        texto=archivo.read()
        print(texto)
        archivo.close()
    elif opcion==2:
        archivo=open("archivo.txt","a")
        nombre=input("Nombre: ")
        telefono=input("Telefono: ")
        mail=input("Email: ")
        archivo.write(nombre+" "+telefono+" "+mail+"\n")
        archivo.close()
    elif opcion==3:
        archivo=open("archivo.txt","r")
        nombre=input("Ingrese el nombre: ")
        for x in archivo.readlines():
            if nombre in x:
                print(x)
            else:
                print(f'El nombre {nombre} no esta en la lista')
                break
        archivo.close()
    elif opcion==4:
        break
    else:
        print("Opcion incorrecta")
archivo.close()
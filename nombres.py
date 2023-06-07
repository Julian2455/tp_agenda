archivo=open("archivo.txt","a")
while True:
    nombre=input("Nombre: ")
    if nombre!="terminar":
        telefono=input("Telefono: ")
        mail=input("Email: ")
        archivo.write(nombre+" "+telefono+" "+mail+"\n")
    else:
        break
archivo=open("archivo.txt","r")
nombre=input("buscar: ")
for x in archivo.readlines():
    if nombre in x:
        print(x)
archivo.close()
print("Escriba un programa al que usted ingrese una frase y el programa muestre en consola estafrase desde el final hasta el principio")
nombre=input("Por favor ingrese su nombre: ")
frase=input(f"Hola {nombre} ingresa la frase: ")


i=len(frase)-1
while i >= 0:
    print(frase[i])
    i -= 1

    

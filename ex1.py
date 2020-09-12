print("Bienvenido a su calculador de potencia")

x = int(input("Ingrese el valor de la base (X): "))
y = int(input("Ingrese la valor de la potencia (Y): "))

def potencia():
    resultado = x ** y
    print (f"{x}^{y} = {resultado}")
 

potencia()
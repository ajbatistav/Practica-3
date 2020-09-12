def pr(a,b):
    while a <= b:
        res = 6 * a
        print (f"{6} X {a} = {res}")
        a += 1

print("Bienvenido")

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero mayor que el anterior: "))

if n1 > n2:
    print(f"{n2} no es mayor que {n1}, regrese a la escuela, BYE")

else:
    pr(n1,n2) 

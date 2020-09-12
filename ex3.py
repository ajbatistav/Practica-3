def bisiesto():
 year = int(input("ingrese un año: "))
 test = year % 4
 if test == 0:
    print(f"{year} es bisiesto")
 else:
    print(f"{year} no es bisiesto")


bisiesto()
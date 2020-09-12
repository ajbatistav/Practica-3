def bisiesto(year):
  test = year % 4
  if test == 0:
    print(f"{year} es bisiesto")
  else:
    print(f"{year} no es bisiesto")


y= int(input("ingrese un año: "))
bisiesto(y)
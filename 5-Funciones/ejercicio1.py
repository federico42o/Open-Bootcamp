"""Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo."""


alt = int(input("Ingrese la altura del triangulo: "))
b = int(input("Ingrese la base del triangulo: "))

def area_t(base,altura):
    return (base*altura)/2

print(f"Area del triangulo: {area_t(alt,b)} unidades")

radio = int(input("Ingrese el radio del circulo: "))
PI = 3.14
def area_c(radio,pi):
    return pi*radio**2

print(f"Area del circulo: {area_c(radio,PI)} unidades")

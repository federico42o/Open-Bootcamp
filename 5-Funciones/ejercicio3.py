"""Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."""


def es_bisiesto(anio):
    
    if anio % 4 == 0 and (anio % 400 == 0 or anio % 100 != 0):
        return f"{anio} es bisiesto"
    return f"{anio} no es bisiesto"

anio = int(input("Ingrese un año: "))


print(es_bisiesto(anio))
"""Escribe una función que pueda decirte si un número (número entero) es primo o no."""


num = int(input("Ingrese un numero: "))


def es_primo(x):
    if x>1:
        for n in range(2,x):
            if x%n == 0:
                return f"{x} no es un numero primo"
        return f"{x} es un numero primo"       
    return f"Ingrese un numero entero mayor a 1"

print(es_primo(num))

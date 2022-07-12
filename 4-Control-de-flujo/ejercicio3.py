"""Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso."""


lista_nums = [x for x in range(1,101)]
lista_nums.sort(reverse=True)
print(*lista_nums,sep=",")
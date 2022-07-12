num_inicial = int(input("Ingrese un numero inicial: "))
num_final = int(input("Ingrese un numero final: "))


numeros_pares = [x for x in range(num_inicial,num_final+1) if x%2]


print(numeros_pares)
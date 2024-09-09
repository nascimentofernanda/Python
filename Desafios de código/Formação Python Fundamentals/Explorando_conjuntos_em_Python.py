#Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

def elementos_comuns(listas):
    conjunto1 = set(lista1)  
    conjunto2 = set(lista2) 
    comuns = conjunto1.intersection(conjunto2) 
    return list(comuns)

lista1 = input().split()
lista2 = input().split()

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
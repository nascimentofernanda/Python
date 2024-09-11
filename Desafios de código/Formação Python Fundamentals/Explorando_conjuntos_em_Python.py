#Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

def encontrar_comuns(lista1, lista2):  
    # Converter as listas em conjuntos para eliminar duplicatas e encontrar interseção  
    conjunto1 = set(lista1)  
    conjunto2 = set(lista2)  
    
    # Encontrar os elementos comuns entre os conjuntos  
    comuns = conjunto1.intersection(conjunto2)  
    
    # Converter o resultado de volta para uma lista e retornar  
    return list(comuns)  

def entrada_valida(entrada):  
    # Verifica se a entrada é uma sequência de números inteiros  
    try:  
        # Tenta converter cada número para inteiro  
        lista = list(map(int, entrada.split()))  
        return lista, True  
    except ValueError:  
        # Retorna um valor inválido  
        return [], False  

# Exemplo de uso:  
entrada1 = input("Digite a primeira lista de números inteiros separados por espaço: ")  
lista1, valido1 = entrada_valida(entrada1)  

entrada2 = input("Digite a segunda lista de números inteiros separados por espaço: ")  
lista2, valido2 = entrada_valida(entrada2)  

if valido1 and valido2:  
    resultado = encontrar_comuns(lista1, lista2)  
    print("Elementos comuns:", resultado)  
else:  
    print("Entrada inválida.")  
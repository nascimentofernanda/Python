#Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. 
# A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. 
# O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.

def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
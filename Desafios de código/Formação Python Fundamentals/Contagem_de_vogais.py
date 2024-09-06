#Neste desafio, implemente uma solução para completar a função conta_vogais que conta o número de vogais em uma string fornecida como entrada. 
# Vogais são caracteres específicos sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas (aeiouAEIOU).

def conta_vogais(texto):  
    vogais = "aeiouAEIOU"  
    contador = 0  
    
    for char in texto:  
        if char in vogais:  
            contador += 1  
            
    return contador  

entrada = input()

resultado = conta_vogais(entrada)
print(f"O número de vogais na string '{entrada}' é: {resultado}")
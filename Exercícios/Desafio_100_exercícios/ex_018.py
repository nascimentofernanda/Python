# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo=float(input("Digite o ângulo \n"))
seno=math.sin(angulo)
cosseno=math.cos(angulo)
tangente=math.tan(angulo)

print(f'Seno:{seno}, cosseno:{cosseno} e tangente:{tangente}.')
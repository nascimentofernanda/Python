#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

número=float(input('Digite um número \n'))
parte_inteira=math.trunc(número)
print(f'A parte inteira de {número} é {parte_inteira}')


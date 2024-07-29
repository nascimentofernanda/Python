#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno_1=str(input('Primeiro aluno \n'))
aluno_2=str(input('Segundo aluno \n'))
aluno_3=str(input('Terceiro aluno \n'))
aluno_4=str(input('Quarto aluno \n'))
lista=[aluno_1,aluno_2,aluno_3,aluno_4]
aluno_escolhido=random.shuffle(lista)

print(f'A ordem de apresentação será: {lista}.')
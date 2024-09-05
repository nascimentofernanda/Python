# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno_1=str(input('Primeiro aluno \n'))
aluno_2=str(input('Segundo aluno \n'))
aluno_3=str(input('Terceiro aluno \n'))
aluno_4=str(input('Quarto aluno \n'))
lista=[aluno_1,aluno_2,aluno_3,aluno_4]
aluno_escolhido=random.choice(lista)

print(f'O aluno escolhido foi: {aluno_escolhido}.')
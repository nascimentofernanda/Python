#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
número = int(input('Digite o número que deseja calcular a tabuada \n'))
n=1

for i in range(1,11):
    print(f'{número}x{n}={número*n}')
    n=n+1
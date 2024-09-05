#Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela
teste = input('Digite algo \n')
print(type(teste))
print(f'{teste} é um número?', teste.isnumeric())
print(f'{teste} é uma string?', teste.isalpha())
print(f'{teste} é um alfanumérico?', teste.isalpha())
print(f'{teste} é um número decimal?', teste.isdecimal())
print(f'{teste} está escrito em caixa alta?', teste.isupper())
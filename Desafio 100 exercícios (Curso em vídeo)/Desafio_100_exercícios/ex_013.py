#Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salario \n'))
novo_salario = (salario + (salario * 0.15))
print(f'O seu novo salário é R$ {novo_salario:,.2f}')
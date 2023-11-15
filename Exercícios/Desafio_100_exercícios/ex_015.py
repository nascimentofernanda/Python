#Faça um programa e que o usuário digite o número de dias em que alugou um carro e a quantidade de Km rodados e o programa calcule o valor a pagar
dias=int(input('Quantos dias de aluguel? \n'))
kilometros=float(input('Quantos Km foram rodados? \n'))
#Nesse caso foram definidos uma taxa de R$ 80,00 por dia de aluguel + R$ 20,00 por Km rodado.
diária=80.00
taxa_por_km=20.00
valor_total=float((dias*diária)+(taxa_por_km*kilometros))
print(f'O total a pagar é R$ {valor_total:,.2f}')
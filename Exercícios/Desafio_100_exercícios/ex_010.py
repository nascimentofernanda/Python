#Crie um programa que leia um valor em real e converta para dólares - Considere US$ 1,00=R$ 3,27
real = float(input('Digite o valor em reais \n'))
dólar=int(real//3.27)
print(f'Você pode comprar {dólar} dólares')

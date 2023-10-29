#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o preço do produto \n'))
novo_preco = (preco - (preco * 0.05))
print(f'O novo preço do produto com desconto é {novo_preco}')
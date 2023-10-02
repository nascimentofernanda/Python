#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Digite a altura \n'))
largura = float(input('digite a largura \n'))
área = altura * largura
quantidade_de_tinta = área/2
print(f'A quantidade necessária de tinra é {quantidade_de_tinta} litros')
# Em um jogo de RPG, os personagens geralmente possuem uma lista de itens que podem ser utilizados durante o jogo. 
# Esses itens podem ser armas, armaduras, poções de cura, entre outros. 
# É importante que o jogador tenha um controle desses itens para poder utilizá-los no momento adequado.
# Crie um programa que permita cadastrar uma lista de itens que o personagem possui. 
# A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

itens = []
x=0

while x<=2:
    itens.append(input())
    x=x+1

print("Lista de itens:")
for item in itens:
    print(f"- {item}")
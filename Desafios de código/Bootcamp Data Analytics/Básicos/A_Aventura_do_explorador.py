#Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. 
# Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código 
# em Python. Prepare-se para a "Aventura do Explorador"!

número_de_passos=int(input())
while número_de_passos <0:
    número_de_passos=int(input())

if número_de_passos ==0 :
   print("Nenhum passo dado na floresta.")
elif número_de_passos ==1 :
    print("Explorador: 1 passo")
elif número_de_passos >1 :
    print("Explorador: 1 passo")
    x=2
    while x<= número_de_passos:
        print(f"Explorador:", x ,"passos")
        x=x+1
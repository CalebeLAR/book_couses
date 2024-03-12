# 5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi
# feito no Exercício 5.3, e escreva uma cadeia if-else.
# • Se a cor do alienígena for verde, mostre uma frase informando que o jogador
# acabou de ganhar cinco pontos por atingir o alienígena.
# • Se a cor do alienígena não for verde, mostre uma frase informando que o
# jogador acabou de ganhar dez pontos.
# • Escreva uma versão desse programa que execute o bloco if e outro que
# execute o bloco else.

alien_color = "green"


# versão que execute o bloco if
if alien_color == "green":
    print("You just received 5 points!")
if alien_color != "green":
    print("You just received 10 points!")

# versão que execute o bloco else
if alien_color == "green":
    print("You just received 5 points!")
else:
    print("You just received 10 points!")

# 5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
# em uma cadeia if-elif-else.
# • Se o alienígena for verde, mostre uma mensagem informando que o jogador
# ganhou cinco pontos.
# • Se o alienígena for amarelo, mostre uma mensagem informando que o
# jogador ganhou dez pontos.
# • Se o alienígena for vermelho, mostre uma mensagem informando que o
# jogador ganhou quinze pontos.
# • Escreva três versões desse programa, garantindo que cada mensagem seja
# exibida para a cor apropriada do alienígena.

alien_color = "green"


# versão que executa o bloco if
if alien_color == "green":
    print("You just received 5 points!")

if alien_color == "yellow":
    print("You just received 10 points!")

if alien_color == "red":
    print("You just received 15 points!")


# versão que executa o bloco if-elif
if alien_color == "green":
    print("You just received 5 points!")
elif alien_color == "yellow":
    print("You just received 10 points!")
elif alien_color == "red":
    print("You just received 15 points!")


# versão que executa o bloco if-elif-else
if alien_color == "green":
    print("You just received 5 points!")
elif alien_color == "yellow":
    print("You just received 10 points!")
else:
    print("You just received 15 points!")

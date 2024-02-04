# 4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
# acrescente várias linhas no final do programa que façam o seguinte:
# • Exiba a mensagem. "Os três primeiros itens da lista". Em seguida, use
# uma fatia para exibir os três primeiros itens da lista desse programa.
# • Exiba a mensagem "Os Três itens do meio da lista são:" Em siguida, use uma
# fatia para exibir três itens do meio da lista.
# • Exiba a mensagem "Os três últimos itens da lista são:". Use uma fatia para
# exibir os três últimos itens da lista.


def main():
    pizza = ["pepperoni", "mushrooms", "onions", "peppers", "sausage"]

    print("Os três primeiros itens da lista")
    print(pizza[0:3])

    print("Os Três itens do meio da lista são:")
    print(pizza[2:5])

    print("Os três últimos itens da lista são:")
    print(pizza[2:6])


if __name__ == "__main__":
    main()

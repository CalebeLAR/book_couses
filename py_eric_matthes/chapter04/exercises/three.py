# 4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
# exibir os números de sua lista.


def main():
    three = list([num * 3 for num in range(3, 31, 2)])
    print(three)


if __name__ == "__main__":
    main()

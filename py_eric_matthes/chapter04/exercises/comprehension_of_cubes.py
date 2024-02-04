# 4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
# dos dez primeiros cubos.


def main():
    cubos = [value**3 for value in range(1, 11)]
    print(cubos)


if __name__ == "__main__":
    main()

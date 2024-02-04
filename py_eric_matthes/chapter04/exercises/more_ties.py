# 4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
# laços for para fazer exibições a fim de economizar espaço. Escolha uma
# versão de foods.py e escreva dois laços for para exibir cada lista de comidas.


def main():
    foods = ["pizza", "falafel", "carrot cake"]
    for food in foods:
        print(food)

    for food in foods:
        print(f"Gosto de: {food}.")

    print("Otimas comidas")


if __name__ == "__main__":
    main()

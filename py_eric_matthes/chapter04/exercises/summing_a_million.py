# 4.5 – Somando um milhao: Crie uma lista de números de um a um milhão e, em
# seguida, use min() e max() para garantir que sua lista realmente começa em um
# e termina em um milhão. Além disso, utilize a função sum() para ver a rapidez
# com que Python é capaz de somar um milhão de números


def main():
    numbers = list(range(1, 1000001))
    print(f"Min: {min(numbers)}")  # Min: 1
    print(f"Max: {max(numbers)}")  # Max: 1000000
    print(f"Sum: {sum(numbers)}")  # Sum: 500000500000


if __name__ == "__main__":
    main()

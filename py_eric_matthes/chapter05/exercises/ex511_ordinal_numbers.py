# 5.11 – Números ordinais: Números ordinais indicam sua posição em uma lista,
# por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa
# língua termina com th, exceto 1, 2 e 3.
# • Armazene os números de 1 a 9 em uma lista.
# • Percorra a lista com um laço.
# • Use uma cadeia if-elif-else no laço para exibir a terminação apropriada
# para cada número ordinal. Sua saída deverá conter "1st 2nd 3rd 4th 5th
# 6th 7th 8th 9th", e cada resultado deve estar em uma linha separada.

ordinal_numbers = list(range(1, 10))

for ordinal_number in ordinal_numbers:
    if ordinal_number > 3:
        # economiza processamento escrever primeiro a condicional mais frequente # noqa 
        print(f"{ordinal_number}th")

    elif ordinal_number == 1:
        print(f"{ordinal_number}st")

    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")

    else:
        print(f"{ordinal_number}rd")

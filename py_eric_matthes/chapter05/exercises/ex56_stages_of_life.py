# 5.6 – Estágios da vida: Escreva uma cadeia if-elif-else que determine o
# estágio da vida de uma pessoa. Defina um valor para a variável age e então:
# • Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
# que ela é um bebê.
# • Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma
# mensagem dizendo que ela é uma criança.
# • Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma
# mensagem dizendo que ela é um(a) garoto(a).
# • Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
# mensagem dizendo que ela é um(a) adolescente.
# • Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
# mensagem dizendo que ela é adulto.
# • Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
# pessoa é idoso.

age = int(input("Enter your age: "))

if age < 2:
    print("You're a baby!")
elif age >= 2 and age < 4:
    print("You're a toddler!")
elif age >= 4 and age < 13:
    print("You're a kid!")
elif age >= 13 and age < 20:
    print("You're a teenager!")
elif age >= 20 and age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

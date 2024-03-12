# 5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
# criar em dez. Se quiser testar mais comparações, escreva outros testes e
# acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um
# False para cada um dos casos a seguir: • testes de igualdade e de não
# igualdade com strings; • testes usando a função lower(); • testes numéricos que
# envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e
# menor ou igual a; • testes usando as palavras reservadas and e or; • testes
# para verificar se um item está em uma lista; • testes para verificar se um item
# não está em uma lista.

animal1 = "Dog"
animal2 = "Cat"
animals = ["dog", "cat", "bird"]

# usa a função min() para descobrir o animal com menos letras da lista animals. # noqa
smallest = min(animals, key=len)

if animal1 == animal2:
    print("The animals are the same.")

if animal1 != animal2:
    print("The animals are not the same.")

if animal1.lower() in animals:
    print("The animal is in the list.")

if animal2.lower() not in animals:
    print("The animal is not in the list.")

if len(animal1) > len(animal2):
    print("The first animal is longer.")

if len(animal2) < len(animal1):
    print("The second animal is longer.")

if len(animal1) == len(animal2):
    print("The animals are the same length.")

if len(animal1) <= len(smallest):
    print("The first animal is shorter")

if len(animal2) >= len(smallest):
    print("The second animal is biggest")

if animal1.lower() in animals and animal2.lower() in animals:
    print("The animals are in the list")

if animal1.lower() in animals or animal2.lower() in animals:
    print("At least one of the animals is in the list")

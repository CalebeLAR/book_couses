# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
# dois convidados.

# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas
# pessoas para o jantar.

# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
# que apenas dois nomes permaneçam em sua lista. Sempre que remover um
# nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
# saiba que você sente muito por não poder convidá-la para o jantar.

guests = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]

guest_cannot_attend = "Nelson Mandela"
new_guest = "Marie Curie"

print(guest_cannot_attend + " não poderá comparecer!")

guests.remove(guest_cannot_attend)
guests.append(new_guest)

print("Olá " + guests[0] + "! Espero que possa comparecer.")
print("Olá " + guests[1] + "! Gostaria de convidá-lo para jantar.")
print("Olá " + guests[2] + "! Gostaria de convidá-lo para jantar.")

print(guests)
print("temos mais convidados")

guests.insert(0, "Charles Darwin")
guests.insert(3, "Jane Goodall")
guests.append("Stephen Hawking")

print("Olá " + guests[0] + "! Espero que possa comparecer.")
print("Olá " + guests[1] + "! Gostaria de convidar você para jantar.")
print("Olá " + guests[2] + "! Gostaria de convidar você para jantar.")
print("Olá " + guests[3] + "! Espero que possa comparecer.")
print("Olá " + guests[4] + "! Espero que possa comparecer.")
print("Olá " + guests[5] + "! Gostaria de convidar você para jantar.")

print("Agorá so poderão aparecer duas pessoas")
albert_einstein = guests.pop(1)
ada_lovelace = guests.pop(1)
jane_goodall = guests.pop(1)
marie_curie = guests.pop(1)

print(albert_einstein + "sinto muito por não poder te convidar para o jantar")
print(ada_lovelace + "sinto muito por não poder te convidar para o jantar")
print(jane_goodall + "sinto muito por não poder te convidar para o jantar")
print(marie_curie + "sinto muito por não poder te convidar para o jantar")

print("Olá " + guests[0] + "! Espero que possa comparecer.")
print("Olá " + guests[1] + "! Gostaria de convidar você para jantar.")

del guests[0]
del guests[0]

print(guests)

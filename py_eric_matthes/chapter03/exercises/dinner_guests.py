# 3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
# Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma
# mensagem informando o número de pessoas que você está convidando para o
# jantar.
guests = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]
print("numero de convidados: ", len(guests), "\n")

guest_cannot_attend = "Nelson Mandela"
new_guest = "Marie Curie"

print(guest_cannot_attend + " não poderá comparecer!")

guests.remove(guest_cannot_attend)
print("numero de convidados: ", len(guests), "\n")

guests.append(new_guest)
print("numero de convidados: ", len(guests), "\n")


print("Olá " + guests[0] + "! Espero que possa comparecer.")
print("Olá " + guests[1] + "! Gostaria de convidá-lo para jantar.")
print("Olá " + guests[2] + "! Gostaria de convidá-lo para jantar.")

print(guests)
print("temos mais convidados")

guests.insert(0, "Charles Darwin")
print("numero de convidados: ", len(guests), "\n")
guests.insert(3, "Jane Goodall")
print("numero de convidados: ", len(guests), "\n")
guests.append("Stephen Hawking")
print("numero de convidados: ", len(guests), "\n")

print("Olá " + guests[0] + "! Espero que possa comparecer.")
print("Olá " + guests[1] + "! Gostaria de convidar você para jantar.")
print("Olá " + guests[2] + "! Gostaria de convidar você para jantar.")
print("Olá " + guests[3] + "! Espero que possa comparecer.")
print("Olá " + guests[4] + "! Espero que possa comparecer.")
print("Olá " + guests[5] + "! Gostaria de convidar você para jantar.\n")

print("Agorá so poderão aparecer duas pessoas")
albert_einstein = guests.pop(1)
print(albert_einstein + "sinto muito por não poder te convidar para o jantar")
print("numero de convidados: ", len(guests), "\n")

ada_lovelace = guests.pop(1)
print(ada_lovelace + "sinto muito por não poder te convidar para o jantar")
print("numero de convidados: ", len(guests), "\n")

jane_goodall = guests.pop(1)
print(jane_goodall + "sinto muito por não poder te convidar para o jantar")
print("numero de convidados: ", len(guests), "\n")

marie_curie = guests.pop(1)
print(marie_curie + "sinto muito por não poder te convidar para o jantar")
print("numero de convidados: ", len(guests), "\n")


print("Olá " + guests[0] + "! Espero que possa comparecer.")
print("Olá " + guests[1] + "! Gostaria de convidar você para jantar.\n")

del guests[0]
print("numero de convidados: ", len(guests), "\n")

del guests[0]
print("numero de convidados: ", len(guests), "\n")

print(guests)

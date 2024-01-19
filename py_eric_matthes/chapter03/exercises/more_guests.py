# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados
# para o jantar.
# • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
# uma instrução print no final de seu programa informando às pessoas que
# você encontrou uma mesa de jantar maior.

# • Utilize insert() para adicionar um novo convidado no início de sua lista.
# • Utilize insert() para adicionar um novo convidado no meio de sua lista.
# • Utilize append() para adicionar um novo convidado no final de sua lista.
# • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
# que está em sua lista.

index = 1

guests = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]
guest_cannot_attend = guests.pop(index)

print(guest_cannot_attend + " não poderá comparecer!")

new_guest = "Marie Curie"
guests.insert(index, new_guest)

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
print("Olá " + guests[4] + "! Gostaria de convidar você para jantar.")
print("Olá " + guests[5] + "! Gostaria de convidar você para jantar.")

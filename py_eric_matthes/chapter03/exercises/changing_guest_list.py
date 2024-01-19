# 3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para
# convidar.

# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não
# poderá comparecer.

# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.

# • Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.

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

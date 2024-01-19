# 3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
# você gostaria de visitar.

# • Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
# em ordem alfabética.
lugares_para_visitar = ["Tóquio", "Machu Picchu", "Paris", "Grand Canyon", "Sydney"]

# • Exiba sua lista na ordem original. Não se preocupe em exibi-la como uma
# lista Python pura; basta exibi-la como uma lista de locais.
print("Lista na ordem original:")
print(lugares_para_visitar)

# • Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
# lista propriamente dita.
print("\nLista em ordem alfabética:")
print(sorted(lugares_para_visitar))

# • Mostre que sua lista manteve sua ordem original exibindo-a.
print("\nLista na ordem original:")
print(lugares_para_visitar)

# • Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
# a ordem da lista original.
print("\nLista em ordem alfabética inversa:")
print(sorted(lugares_para_visitar, reverse=True))

# • Mostre que sua lista manteve sua ordem original exibindo-a novamente.
print("\nLista na ordem original:")
print(lugares_para_visitar)

# • Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
# que sua ordem mudou.
lugares_para_visitar.reverse()
print("\nLista com a ordem invertida:")
print(lugares_para_visitar)

# • Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista
# para mostrar que ela voltou à sua ordem original.
lugares_para_visitar.reverse()
print("\nLista com a ordem revertida novamente:")
print(lugares_para_visitar)

# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
# ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
lugares_para_visitar.sort()
print("\nLista em ordem alfabética:")
print(lugares_para_visitar)

# • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
# ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
lugares_para_visitar.sort(reverse=True)
print("\nLista em ordem alfabética inversa:")
print(lugares_para_visitar)

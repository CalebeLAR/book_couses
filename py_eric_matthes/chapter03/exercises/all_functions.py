# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
# lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
# cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
# crie uma lista contendo esses itens e então utilize cada função apresentada
# neste capítulo pelo menos uma vez.

names = ["luffy", "zoro", "robin", "usop", "chopper", "nami", "frank", "brook"]
guests = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]
vehicles = ["motocicleta", "carro", "bicicleta", "ônibus", "avião", "barco"]
places_to_explore = ["Tóquio", "Machu Picchu", "Paris", "Grand Canyon", "Sydney"]

tot_names = len(names)
tot_guests = len(guests)
tot_vehicles = len(vehicles)
tot_places_to_explore = len(places_to_explore)

all_itens = []
all_itens.append(names[0])
all_itens.append(names[1])
all_itens.append(names[2])
all_itens.append(names[3])
all_itens.append(names[4])
all_itens.append(names[5])
all_itens.append(names[6])
all_itens.append(names[7])

all_itens.insert(0, guests[0])
all_itens.insert(1, guests[1])
all_itens.insert(2, guests[2])

motorcycle = vehicles.pop(0)
car = vehicles.pop(0)
bicycle = vehicles.pop(0)
bus = vehicles.pop(0)
airplane = vehicles.pop(0)
boat = vehicles.pop(0)

all_itens.append(motorcycle)
all_itens.append(car)
all_itens.append(bicycle)
all_itens.append(bus)
all_itens.append(airplane)
all_itens.append(boat)

all_itens.append(places_to_explore[0])
del places_to_explore[0]

all_itens.append(places_to_explore[0])
del places_to_explore[0]

all_itens.append(places_to_explore[0])
del places_to_explore[0]

all_itens.append(places_to_explore[0])
del places_to_explore[0]

all_itens.append(places_to_explore[0])
del places_to_explore[0]

print(all_itens)
print(
    "tamanho de names: " + str(tot_names),
    "\n",
    "tamanho de guests: " + str(tot_guests),
    "\n",
    "tamanho de vehicles: " + str(tot_vehicles),
    "\n",
    "tamanho de places_to_explore: " + str(tot_places_to_explore),
    "\n",
    "total = ",
    tot_names + tot_guests + tot_vehicles + tot_places_to_explore,
    "tamanho de all_itens: " + str(len(all_itens)),
)

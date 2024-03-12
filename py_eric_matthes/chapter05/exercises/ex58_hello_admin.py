# 5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários,
# incluindo o nome 'admin'. Suponha que você esteja escrevendo um código
# que exibirá uma saudação a cada usuário depois que eles fizerem login
# em um site. Percorra a lista com um laço e mostre uma saudação para
# cada usuário:
# • Se o nome do usuário for 'admin', mostre uma saudação especial,
# por exemplo, Olá admin, gostaria de ver um relatório de status?
# • Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
# fazer login novamente.

users = ["admin", "user1", "user2", "user3", "user4"]
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

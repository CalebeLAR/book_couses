# 5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir
# que a lista de usuários não esteja vazia.
# • Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
# usuários!
# • Remova todos os nomes de usuário de sua lista e certifique-se de que a
# mensagem correta seja exibida.

users = []

if not users:
    print("Precisamos encontrar alguns usuários!")

for user in users:  # o python pula o for se a lista for vazia.
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

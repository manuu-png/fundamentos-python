def login():
    usuario = input("digite o usuário: ")
    senha = input("digite a senha: ")

    if usuario == "admin" and senha == "1234":
        print("login realizado com sucesso")
    elif usuario == "admin":
        print("senha incorreta")
    else:
        print("usuário não encontrado")


login()
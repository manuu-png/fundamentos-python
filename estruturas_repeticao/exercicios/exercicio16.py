def validar_senha(senha_correta):
    tentativas = 3

    while tentativas > 0:
        senha_digitada = input("Digite a senha: ")
        if senha_digitada == senha_correta:
            print("Acesso permitido!")
            return
        else:
            tentativas -= 1
            print(f"Senha incorreta! Tentativas restantes: {tentativas}")

    print("Acesso bloqueado!")

validar_senha("1234")
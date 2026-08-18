def verificar_senha():
    senha = input("digite a senha: ")

    if senha == "python123":
        print(f"acesso permitido")
    else:
        print(f"senha inválida")

verificar_senha()
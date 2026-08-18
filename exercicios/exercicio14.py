def votacao():
    idade = int(input("Digite a sua idade: "))

    if idade < 16:
        print(f"não pode votar")
    elif idade < 18 or idade >= 70:
        print(f"voto opcional")
    else:
        print(f"voto obrigatório")


votacao()
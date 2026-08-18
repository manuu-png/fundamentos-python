def faixaetaria():
    idade = int(input("digite sua idade: "))

    if idade <= 12:
        print(f"criança")
    elif idade <= 17:
        print(f"adolescente")
    elif idade <= 59:
        print(f"adulto")
    else:
        print(f"idoso")
faixaetaria()
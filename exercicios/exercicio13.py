def calcular_ingresso():
    idade = int(input("Digite a idade: "))

    if idade <= 5:
        print(f"Preço do ingresso: Gratuito")
    elif 6 <= idade <= 12:
        print(f"Preço do ingresso: R$ 10,00")
    elif 13 <= idade <= 59:
        print(f"Preço do ingresso: R$ 20,00")
    else:
        print(f"Preço do ingresso: R$ 10,00")

calcular_ingresso()

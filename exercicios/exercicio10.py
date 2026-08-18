def calcular():
    valor = float(input("digite o valor da compra (R$): "))

    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.15

    valor_final = valor - desconto
    print(f"valor com desconto: R$ {valor_final:.2f}")


calcular()
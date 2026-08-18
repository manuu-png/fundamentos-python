def analisar_numero():
    numero = int(input("Número: "))

    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    if sinal == "zero":
        print("Classificação: zero e par")
    else:
        print(f"Classificação: {sinal} e {paridade}")

analisar_numero()
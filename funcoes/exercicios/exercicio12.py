def calculardesconto():
    produto = float(input("Digite o valor do produto: "))
    desconto = float(input("Digite o valor do desconto: "))

    valor_desconto = produto * (desconto / 100)
    valor_final = produto - valor_desconto
    print(f"O valor do produto foi de: R$ {valor_desconto} reais")
    return valor_final

calculardesconto()
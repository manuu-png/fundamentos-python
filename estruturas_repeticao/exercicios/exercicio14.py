def calcular_media():
    soma = 0
    quantidade = 0

    while True:
        numero = float(input("Digite um número (ou 0 para encerrar): "))
        if numero == 0:
            break
        soma += numero
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"A média dos {quantidade} números digitados é: {media:.2f}")
    else:
        print("Nenhum número válido foi digitado.")


calcular_media()
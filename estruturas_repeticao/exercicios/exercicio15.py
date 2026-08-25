def maior_numero():
    maior = None

    while True:
        numero = float(input("digite um número (0 para parar): "))

        if numero == 0:
            break

        if maior is None or numero > maior:
            maior = numero

    print("Maior número é:", maior)


maior_numero()

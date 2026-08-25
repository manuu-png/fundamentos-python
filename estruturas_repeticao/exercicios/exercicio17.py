def jogo_adivinhacao(numero_secreto):
    while True:
        numero = int(input("digite seu palpite: "))

        if numero == numero_secreto:
            print("você acertou!")
            break

        elif numero < numero_secreto:
            print("o número é maior")

        else:
            print("o número é menor")


jogo_adivinhacao(67)
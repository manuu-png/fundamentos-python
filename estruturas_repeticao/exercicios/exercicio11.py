def fatorial(numero):
    total = 1

    for valor in range(1, numero + 1):
        total *= valor
    return total

numero1 = int(input("Digite um número fatorial: "))


if numero1 < 0:
    print("Não existe fatorial de número negativo!")
else:
    resultado = fatorial(numero1)
    print(f"O fatorial de {numero1} é {resultado}")

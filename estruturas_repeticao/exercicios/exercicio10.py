def somar_pares(inicio, fim):
    total = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            total += numero
    return total


inicio1 = int(input("Digite o número inicial: "))
fim2 = int(input("Digite o número final: "))


resultado = somar_pares(inicio1, fim2)

print(f"a soma dos numeros pares é {resultado}")

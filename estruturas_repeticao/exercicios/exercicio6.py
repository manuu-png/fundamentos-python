def somar_ate(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma


limite = int(input("digite um número inteiro: "))
resultado = somar_ate(limite)
print(f"a soma de todos os números de 1 até {limite} é: {resultado}")

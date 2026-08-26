def somar_numeros(numeros):
    total = sum(numeros)
    print(f'a soma dos números é {total}')
    return total


numeros = []

quantidade = int(input('quantos números deseja adicionar? '))

for i in range(quantidade):
    numero = int(input('digite um número: '))
    numeros.append(numero)

somar_numeros(numeros)
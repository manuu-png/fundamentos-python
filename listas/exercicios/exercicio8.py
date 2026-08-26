def ordenar_numeros(numeros):
    numeros_ordenados = sorted(numeros)
    print(f'a lista ordenada é {numeros_ordenados}')
    return numeros_ordenados


numeros = []

quantidade = int(input('quantos números deseja adicionar? '))

for i in range(quantidade):
    numero = int(input('digite um número: '))
    numeros.append(numero)

ordenar_numeros(numeros)
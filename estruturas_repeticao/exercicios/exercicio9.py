def contar_pares(inicio, fim):
    quantidade = 0
    for c in range(inicio, fim + 1):
        if c % 2 == 0:
            quantidade = quantidade + 1

    return quantidade

inicio = int(input('digite o inicio: '))
fim = int(input('digite o fim: '))

resultado = contar_pares(inicio, fim)
print('quantidade de numeros pares:', resultado)

contar_pares(inicio, fim)
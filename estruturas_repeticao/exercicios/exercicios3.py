def mostrar_pares():
    pares = int(input('digite um numero: '))
    for i in range(1, pares + 1):
        if i % 2 == 0:
            print(i)


mostrar_pares()
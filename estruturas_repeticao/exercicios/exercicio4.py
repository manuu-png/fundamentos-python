def mostrar_impares():
    impares = int(input('digite um numero: '))
    for i in range(1, impares + 1):
        if i % 2 != 0:
            print(i)
            
mostrar_impares()
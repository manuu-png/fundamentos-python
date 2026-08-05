def numeros():
    numero = int(input('digite um numero: '))
    dobro = numero * 2
    triplo = numero * 3
    print(f'o triplo do {numero} é {triplo} e o dobro é {dobro}')
    return numero

numeros()
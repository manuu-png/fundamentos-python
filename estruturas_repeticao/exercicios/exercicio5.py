def tabuada():
    multiplicador = int(input('digite um numero :'))
    for numero in range(1,11):
        print(f'{multiplicador} x {numero} = {multiplicador*numero}')

tabuada()
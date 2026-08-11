def consumo():
    energia = float(input('Digite o valor do consumo de energia: '))
    valor = float(input('Digite o valor da energia: '))

    conta = energia * valor
    print(f'o valor da conta é de: {conta}')
    return conta

consumo()
def prestacao():
    produto = float(input('Digite o valor do produto: '))
    parcela = float(input('Digite a quantidade de parcelas: '))

    valor = produto / parcela
    print(f'o valor da parcela é de: {valor}')
    return valor

prestacao()
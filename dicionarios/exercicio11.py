def reajustar_preco():
    produto = {}

    produto['nome'] = input('informe o nome do produto: ')
    produto['preco'] = float(input('informe o preço: '))

    aumento = float(input('informe o percentual de aumento: '))

    produto['preco'] += produto['preco'] * aumento / 100

    print(f'novo preço: R$ {produto["preco"]:.2f}')


reajustar_preco()
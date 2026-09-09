def atualizar_estoque():
    produto = {}

    produto['nome'] = input('informe o nome do produto: ')
    produto['preco'] = float(input('informe o preço: '))
    produto['estoque'] = int(input('informe o estoque: '))

    quantidade = int(input('quantidade vendida: '))

    if quantidade <= produto['estoque']:
        produto['estoque'] -= quantidade
        print('estoque atualizado:', produto['estoque'])
    else:
        print('quantidade maior que o estoque')


atualizar_estoque()
def lista_compras():
    compra = {
        'cliente': input('informe o nome do cliente: '),
        'produtos': []
    }

    for produto in range(5):
        nome = input(f'digite o produto {produto + 1}: ')
        compra['produtos'].append(nome)

    print('cliente:', compra['cliente'])
    print('produtos comprados:')

    for produto in compra['produtos']:
        print(produto)


lista_compras()
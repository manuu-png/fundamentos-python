def encontrar_produto(produtos, produto):
    if produto not in produtos:
        print('produto não encontrado')
    else:
        posicao = produtos.index(produto)
        print(f'a posição do produto {produto} é {posicao}')
        return posicao


produtos = ['arroz', 'feijão', 'macarrão', 'café']

produto = input('digite o produto que deseja encontrar: ')

encontrar_produto(produtos, produto)
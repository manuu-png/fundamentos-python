def remover_produto(produtos, produto):
    if produto not in produtos:
        print('este produto não existe na lista')
    else:
        produtos.remove(produto)
        print(f'o produto {produto} foi removido da lista: {produtos}')


produtos = ['arroz', 'feijão', 'macarrão', 'café']

produto = input('digite o produto que deseja remover: ')

remover_produto(produtos, produto)
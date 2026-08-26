def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
    print(f'os novos produtos foram adicionados à lista: {compras}')


def cancelar_compra(compras, produto):
    if produto not in compras:
        print('este produto não está na lista de compras')
    else:
        compras.remove(produto)
        print(f'o produto {produto} foi removido da lista: {compras}')


compras = []

produtos = []

quantidade = int(input('quantos produtos deseja adicionar? '))

for i in range(quantidade):
    produto = input('digite o produto: ')
    produtos.append(produto)

adicionar_produtos(compras, produtos)

produto_cancelar = input('digite o produto que deseja cancelar: ')

cancelar_compra(compras, produto_cancelar)
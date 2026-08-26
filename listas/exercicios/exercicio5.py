def remover_item(itens, posicao):
    item_removido = itens.pop(posicao)
    print(f'o item {item_removido} foi removido da lista: {itens}')
    return item_removido


itens = ['arroz', 'feijão', 'macarrão', 'café']

posicao = int(input('digite a posição que deseja remover: '))

remover_item(itens, posicao)
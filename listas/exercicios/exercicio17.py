def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print(f'o produto {produto} foi vendido: {estoque}')
    else:
        print('o produto não está disponível')

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

produto = input('digite o produto que deseja vender: ')

vender_produto(estoque, produto)
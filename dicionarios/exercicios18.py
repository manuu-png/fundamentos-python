def cadastrar_produto(produtos):
    produto = {}

    produto['nome'] = input('informe o nome do produto: ')
    produto['preco'] = float(input('informe o preço: '))
    produto['estoque'] = int(input('informe o estoque: '))

    produtos.append(produto)
    print('produto cadastrado!')


def listar_produtos(produtos):
    if len(produtos) == 0:
        print('nenhum produto cadastrado')
    else:
        for produto in produtos:
            print(f'nome: {produto["nome"]}')
            print(f'preço: R$ {produto["preco"]:.2f}')
            print(f'estoque: {produto["estoque"]}')
            print()


def buscar_produto(produtos):
    nome = input('digite o nome do produto: ')

    for produto in produtos:
        if produto['nome'] == nome:
            print('produto encontrado:', produto)
            return

    print('produto não encontrado')


def atualizar_estoque(produtos):
    nome = input('digite o nome do produto: ')

    for produto in produtos:
        if produto['nome'] == nome:
            quantidade = int(input('digite a quantidade: '))
            operacao = input('digite + para aumentar ou - para diminuir: ')

            if operacao == '+':
                produto['estoque'] += quantidade
                print('estoque atualizado')
            elif operacao == '-':
                if quantidade <= produto['estoque']:
                    produto['estoque'] -= quantidade
                    print('estoque atualizado')
                else:
                    print('estoque não pode ficar negativo')
            else:
                print('operação inválida')

            return

    print('produto não encontrado')


def remover_produto(produtos):
    nome = input('digite o nome do produto: ')

    for produto in produtos:
        if produto['nome'] == nome:
            produtos.remove(produto)
            print('produto removido')
            return

    print('produto não encontrado')


def sistema_produtos():
    produtos = []

    while True:
        print('===== SISTEMA DE PRODUTOS =====')
        print('1 - Cadastrar produto')
        print('2 - Listar produtos')
        print('3 - Buscar produto')
        print('4 - Atualizar estoque')
        print('5 - Remover produto')
        print('6 - Sair')

        opcao = input('escolha uma opção: ')

        if opcao == '1':
            cadastrar_produto(produtos)
        elif opcao == '2':
            listar_produtos(produtos)
        elif opcao == '3':
            buscar_produto(produtos)
        elif opcao == '4':
            atualizar_estoque(produtos)
        elif opcao == '5':
            remover_produto(produtos)
        elif opcao == '6':
            print('sistema encerrado')
            break
        else:
            print('opção inválida')


sistema_produtos()
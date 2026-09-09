def criar_cadastro():
    dados = {}

    quantidade = int(input('quantas informações deseja cadastrar? '))

    for item in range(quantidade):
        chave = input('digite o nome da chave: ')
        valor = input(f'digite o valor de {chave}: ')

        dados[chave] = valor

    print('cadastro final:', dados)


criar_cadastro()
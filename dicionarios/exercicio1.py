def cadastro_pessoa():
    pessoa = {}

    pessoa['nome'] = input('informe o nome: ')
    pessoa['idade'] = int(input('informe a idade: '))
    pessoa['telefone'] = input('informe o telefone: ')
    pessoa['endereco'] = input('informe o endereco: ')
    pessoa['cidade'] = input('informe a cidade: ')

    print('nome:', pessoa['nome'])
    print('idade:', pessoa['idade'])
    print('telefone:', pessoa['telefone'])
    print('endereco:', pessoa['endereco'])
    print('cidade:', pessoa['cidade'])


cadastro_pessoa()
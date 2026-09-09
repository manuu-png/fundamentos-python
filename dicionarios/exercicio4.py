def verificar_chave():
    usuario = {}

    usuario['nome'] = input('informe o nome: ')
    usuario['idade'] = int(input('informe a idade: '))
    usuario['email'] = input('informe o email: ')
    usuario['cidade'] = input('informe a cidade: ')

    chave = input('digite o nome da chave que deseja procurar: ')

    if chave in usuario:
        print('essa chave existe no dicionario')
    else:
        print('essa chave nao existe no dicionario')


verificar_chave()
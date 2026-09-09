def login():
    usuario = {}

    usuario['login'] = input('crie seu login: ')
    usuario['senha'] = input('crie sua senha: ')

    login = input('digite seu login: ')
    senha = input('digite sua senha: ')

    if login == usuario['login'] and senha == usuario['senha']:
        print('login realizado com sucesso')
    else:
        print('login ou senha incorretos')


login()
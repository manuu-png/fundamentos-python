def adicionar_informacoes():
    aluno = {}

    aluno['nome'] = input('informe o nome: ')
    aluno['idade'] = int(input('informe a idade: '))

    aluno['email'] = input('informe o email: ')
    aluno['endereco'] = input('informe o endereco: ')
    aluno['telefone'] = input('informe o telefone: ')

    print('nome:', aluno['nome'])
    print('idade:', aluno['idade'])
    print('email:', aluno['email'])
    print('endereco:', aluno['endereco'])
    print('telefone:', aluno['telefone'])


adicionar_informacoes()
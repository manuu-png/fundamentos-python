def remover_telefone():
    funcionario = {}

    funcionario['nome'] = input('informe o nome: ')
    funcionario['idade'] = int(input('informe a idade: '))
    funcionario['cargo'] = input('informe o cargo: ')
    funcionario['salario'] = float(input('informe o salario: '))
    funcionario['telefone'] = input('informe o telefone: ')

    print('antes da remoção:', funcionario)

    telefone = funcionario.pop('telefone')

    print('telefone removido:', telefone)
    print('depois da remoção:', funcionario)


remover_telefone()
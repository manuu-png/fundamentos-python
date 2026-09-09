def limpar_cadastro():
    funcionario = {}

    funcionario['nome'] = input('informe o nome: ')
    funcionario['idade'] = int(input('informe a idade: '))
    funcionario['cargo'] = input('informe o cargo: ')
    funcionario['salario'] = float(input('informe o salario: '))
    funcionario['telefone'] = input('informe o telefone: ')

    chave = input('qual chave deseja remover? ')

    if chave in funcionario:
        del funcionario[chave]
        print('dicionario atualizado:', funcionario)
    else:
        print('essa chave nao existe')


limpar_cadastro()
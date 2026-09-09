def alterar_informacoes():
    aluno = {}

    aluno['nome'] = input('informe o nome: ')
    aluno['idade'] = int(input('informe a idade: '))
    aluno['telefone'] = input('informe o telefone: ')
    aluno['endereco'] = input('informe o endereco: ')
    aluno['cidade'] = input('informe a cidade: ')
    aluno['nota'] = float(input('informe a nota: '))
    aluno['turma'] = input('informe a turma: ')
    aluno['curso'] = input('informe o curso: ')

    print('antes:', aluno)

    aluno['idade'] = int(input('informe a nova idade: '))
    aluno['cidade'] = input('informe a nova cidade: ')

    print('depois:', aluno)


alterar_informacoes()
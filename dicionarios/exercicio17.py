def cadastrar_alunos():
    alunos = []

    for item in range(5):
        aluno = {}

        aluno['nome'] = input('informe o nome: ')
        aluno['idade'] = int(input('informe a idade: '))
        aluno['nota'] = float(input('informe a nota: '))

        alunos.append(aluno)

    print('--- ALUNOS CADASTRADOS ---')

    for aluno in alunos:
        print('nome:', aluno['nome'])
        print('idade:', aluno['idade'])
        print('nota:', aluno['nota'])
        print()


cadastrar_alunos()
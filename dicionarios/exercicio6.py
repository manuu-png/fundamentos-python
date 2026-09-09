def cadastrar_notas():
    aluno = {}

    aluno['nome'] = input('informe o nome: ')
    aluno['notas'] = []

    for nota in range(3):
        aluno['notas'].append(float(input(f'informe a nota {nota + 1}: ')))

    aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])

    print('aluno:', aluno)


cadastrar_notas()
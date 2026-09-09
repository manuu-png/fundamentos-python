def aluno_notas():
    aluno = {}

    aluno['nome'] = input('informe o nome: ')
    aluno['notas'] = []

    for nota in range(3):
        aluno['notas'].append(float(input(f'informe a nota {nota + 1}: ')))

    media = sum(aluno['notas']) / len(aluno['notas'])

    print('nome:', aluno['nome'])
    print('notas:', aluno['notas'])
    print('maior nota:', max(aluno['notas']))
    print('menor nota:', min(aluno['notas']))
    print('media:', media)


aluno_notas()
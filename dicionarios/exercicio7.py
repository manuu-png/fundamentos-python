def verificar_aprovacao():
    aluno = {}

    aluno['nome'] = input('informe o nome: ')
    aluno['media'] = float(input('informe a media: '))
    aluno['frequencia'] = float(input('informe a frequencia: '))

    if aluno['media'] >= 6 and aluno['frequencia'] >= 75:
        print(f'o aluno {aluno["nome"]} esta aprovado')
    else:
        print(f'o aluno {aluno["nome"]} nao foi aprovado')


verificar_aprovacao()
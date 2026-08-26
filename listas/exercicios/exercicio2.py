def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print(f'o aluno {nome} foi inserido na posição {posicao}: {alunos}')


lista_de_alunos = []

nome = input('digite o nome do aluno: ')
posicao = int(input('digite a posição: '))

inserir_aluno(lista_de_alunos, nome, posicao)
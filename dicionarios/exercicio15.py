def cadastrar_filme():
    filme = {}

    filme['titulo'] = input('informe o titulo: ')
    filme['ano'] = int(input('informe o ano: '))
    filme['genero'] = input('informe o genero: ')
    filme['notas'] = []

    for nota in range(5):
        filme['notas'].append(float(input(f'informe a nota {nota + 1}: ')))

    media = sum(filme['notas']) / len(filme['notas'])

    print('titulo:', filme['titulo'])
    print('ano:', filme['ano'])
    print('genero:', filme['genero'])
    print('notas:', filme['notas'])
    print('media:', media)


cadastrar_filme()
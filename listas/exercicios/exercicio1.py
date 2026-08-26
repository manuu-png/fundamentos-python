def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(f'o nome {nome} foi adicionado à lista')


lista_de_nomes = []

nome = input('digite um nome: ')

adicionar_nome(lista_de_nomes, nome)
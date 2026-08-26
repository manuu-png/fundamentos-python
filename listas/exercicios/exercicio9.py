def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes)
    print(f'a lista ordenada é {lista_de_nomes_ordenados}')
    return lista_de_nomes_ordenados


nomes = []

quantidade = int(input('quantos nomes deseja adicionar? '))

for i in range(quantidade):
    nome = input('digite um nome: ')
    nomes.append(nome)

ordenar_nomes(nomes)
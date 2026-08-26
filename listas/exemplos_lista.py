def mostrar_nomes(nomes):
    for nome in nomes:
        print(f'o nome da lista é: {nome} ')

lista_do_nomes = ['camila', 'luiza', 'maria', 'manu', 'possidonio']
mostrar_nomes(lista_do_nomes)

# adicionando novo nome na lista

def adicionar_nomes(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nomes(lista_do_nomes, 'camilinha')


# adicionando novo nome em uma posição especifica
def adicionar_nome_posiçao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f'o nome {nome} foi inserido na posição {posicao} da lista: {nomes}')

adicionar_nome_posiçao(lista_do_nomes, "niki-aura", 2)


# juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f'os novos nomes {novos_nomes} foram inseridos na lista: {nomes}')

novos_nomes = ['Yasmin', 'Julia']
juntar_nomes(lista_do_nomes, novos_nomes)

# removendo itens da lista
def remover_nomes_pelo_valor(nomes, nome):
    if nome not in nomes:
        print('este nome não existe na lista')
    else:
        nomes.remove(nome)
        print(f'o nome {nome} foi removido da lista: {nomes}')

remover_nomes_pelo_valor(lista_do_nomes, "Manu")

# removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f'O nome da posição {posicao} é {nomes[posicao]}, foi removido!')

remover_nome_pelo_indice(lista_do_nomes, 4)

# descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print('nome nao encontrado')
    else:
        posicao = nomes.index(nome)
        print(f'a posição do nome {nome} é {posicao}')

encontrar_posicao_pelo_valor(lista_do_nomes, "Camilinha")

# contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f'a quantidade de nomes da lista é {quantidade}')

quantidade_de_nomes(lista_do_nomes)

# ordenando os elemestos da lista
def ordernar_nomes(nomes):
    lista_de_nomes_ordenados  = sorted(nomes, reverse=True)
    print(f'a lista ordenada é {lista_de_nomes_ordenados}')

ordernar_nomes(lista_do_nomes)

# operações matematicas
# calcular media

def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = (total / quantidade)
    print(f'a media das notas é {media}')

notas_semestre = [4, 8, 6,5, 10, 9.7]
calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return ordenadas, media

notas_ordenadas, media = gerenciar_notas(notas_semestre, 6.7)
print(f'notas ordenadas = {notas_ordenadas}')
print(f'a media das notas é  {media}')

# lista de lista
def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f'minha lista de produtos : {produtos[0][2]}')



lista_produtos = [
    ['arroz', 2, 32.00],
    ['feijao', 3, 8.50]

]
novo_produtos = ['café', 2, 28.00]
adicionar_produto(lista_produtos, novo_produtos)

def quantidade_total_produtos(produtos):
    quantidade = []

    for produto in produtos:

        quantidade.append(produto[1])

    return sum(quantidade)

quantidade_total_produtos(lista_produtos)
print(f'quantidade de produtos : {quantidade_total_produtos}')

def valor_total_produtos(produtos):
    valores = []
    for produto in produtos:
        valores.append(produto[2])

    return sum(valores)

preco_total_produtos = valor_total_produtos(lista_produtos)
print(f'o valor total dos produtos é {preco_total_produtos}')
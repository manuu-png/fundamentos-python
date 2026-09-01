def adicionar_nota(notas, nota):
    notas.append(nota)
    print(f'nota adicionada: {notas}')


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)
    print(f'nota inserida: {notas}')


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)
    print(f'notas adicionadas: {notas}')


def remover_nota(notas, nota):
    if nota not in notas:
        print('nota não existe')
    else:
        notas.remove(nota)
        print(f'nota removida: {notas}')


def remover_ultima_nota(notas):
    nota = notas.pop()
    print(f'última nota {nota} removida: {notas}')


def encontrar_nota(notas, nota):
    if nota not in notas:
        print('nota não encontrada')
    else:
        print(f'posição: {notas.index(nota)}')


def quantidade_notas(notas):
    print(f'quantidade: {len(notas)}')


def ordenar_notas(notas):
    print(f'notas ordenadas: {sorted(notas)}')


def notas_inversas(notas):
    print(f'ordem inversa: {list(reversed(notas))}')


def somar_notas(notas):
    print(f'soma: {sum(notas)}')


def calcular_media(notas):
    print(f'média: {sum(notas) / len(notas)}')


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

print(f'lista inicial: {notas}')

nova_nota = float(input('digite uma nova nota: '))
adicionar_nota(notas, nova_nota)

nota = float(input('digite a nota: '))
posicao = int(input('digite a posição: '))
inserir_nota(notas, nota, posicao)

novas_notas = []
quantidade = int(input('quantas notas deseja adicionar? '))

for i in range(quantidade):
    novas_notas.append(float(input('digite uma nota: ')))

adicionar_varias_notas(notas, novas_notas)

nota = float(input('digite a nota que deseja remover: '))
remover_nota(notas, nota)

remover_ultima_nota(notas)

nota = float(input('digite a nota que deseja encontrar: '))
encontrar_nota(notas, nota)

quantidade_notas(notas)
ordenar_notas(notas)
notas_inversas(notas)
somar_notas(notas)
calcular_media(notas)
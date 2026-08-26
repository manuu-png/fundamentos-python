def adicionar_nota(notas, nota):
    notas.append(nota)
    print(f'a nota {nota} foi adicionada: {notas}')


def remover_nota(notas, nota):
    if nota not in notas:
        print('esta nota não existe na lista')
    else:
        notas.remove(nota)
        print(f'a nota {nota} foi removida: {notas}')


def media_notas(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade

    print(f'a média das notas é {media}')
    return media


notas = []

quantidade = int(input('quantas notas deseja adicionar? '))

for i in range(quantidade):
    nota = float(input('digite uma nota: '))
    adicionar_nota(notas, nota)

nota_remover = float(input('digite a nota que deseja remover: '))

remover_nota(notas, nota_remover)

media_notas(notas)
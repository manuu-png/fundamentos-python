def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade

    print(f'a média das notas é {media}')
    return media


notas = []

quantidade = int(input('quantas notas deseja adicionar? '))

for i in range(quantidade):
    nota = float(input('digite uma nota: '))
    notas.append(nota)

calcular_media(notas)
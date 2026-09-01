def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    print(f'o ranking é {ranking}')
    return ranking


pontuacoes = []

quantidade = int(input('quantas pontuações deseja adicionar? '))

for i in range(quantidade):
    pontuacao = int(input('digite uma pontuação: '))
    pontuacoes.append(pontuacao)

criar_ranking(pontuacoes)
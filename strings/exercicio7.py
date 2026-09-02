def procurar_palavra(texto, palavra):
    posicao = texto.lower().find(palavra.lower())

    if posicao != -1:
        print(f'a palavra começa na posição {posicao}')
    else:
        print('a palavra não existe no texto')

texto = input('digite um texto: ')
palavra = input('digite uma palavra: ')

procurar_palavra(texto, palavra)
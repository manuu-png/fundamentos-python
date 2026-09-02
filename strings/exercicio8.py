def verificar_palavra(texto, palavra):
    palavra_encontrada = palavra.lower() in texto.lower()

    if palavra_encontrada:
        print('Palavra encontrada!')
    else:
        print('Palavra não encontrada!')

texto = input('digite um texto: ')
palavra = input('digite uma palavra: ')

verificar_palavra(texto, palavra)
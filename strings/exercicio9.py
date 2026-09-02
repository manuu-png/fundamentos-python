def contar_palavras(texto):
    palavras = texto.split()
    quantidade = len(palavras)
    return quantidade

texto = input('digite um texto: ')

print(f'o texto possui {contar_palavras(texto)} palavras')
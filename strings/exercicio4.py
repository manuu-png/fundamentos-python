def limpar_texto(texto):
    texto_limpo = texto.strip()
    return texto_limpo

texto = input('digite um texto com espaços: ')
print(f'texto limpo: {limpar_texto(texto)}')
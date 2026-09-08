def verificar_extensao(nome_arquivo):
    arquivo_valido = nome_arquivo.endswith('.pdf')

    if arquivo_valido:
        print('Arquivo válido.')
    else:
        print('Arquivo inválido.')

nome_arquivo = input('digite o nome do arquivo: ')

verificar_extensao(nome_arquivo)
def formatar_nome(nome):
    nome_formatado = nome.title()
    return nome_formatado

nome = input('digite seu nome completo: ')
print(f'nome formatado: {formatar_nome(nome)}')
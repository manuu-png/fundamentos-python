def limpar_telefone(telefone):
    telefone = telefone.replace('(', '')
    telefone = telefone.replace(')', '')
    telefone = telefone.replace(' ', '')
    telefone = telefone.replace('-', '')

    return telefone

telefone = input('digite seu telefone: ')

print(f'telefone limpo: {limpar_telefone(telefone)}')
def nome_maiusculo(nome):
    nome_maiusculo = nome.upper()
    return nome_maiusculo

nome = input('digite seu nome: ')
print(f'nome em maiusculo: {nome_maiusculo(nome)}')
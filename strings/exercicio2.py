def nome_minusculo(nome):
    nome_minusculo = nome.lower()
    return nome_minusculo

nome = input('digite seu nome: ')
print(f'nome em minusculo: {nome_minusculo(nome)}')
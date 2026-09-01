# dividir uma string em partes
def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input("digite seu nome completo: ")
print(f'nome em partes: {separar_nome(nome_completo)}')

# juntar strings
def criar_nome_completo(partes):
    nome_completo = ",".join(partes)
    return nome_completo

partes_nomes = ['emanuelle', 'correa', 'lange']
print(f'a junção das partes do nome é: {criar_nome_completo(partes_nomes)}')

# verificar o inicio e o final de uma string
def analisar_url(url):
    com_https = url.startswith('https://')
    termina_com_br = url.endswith('.br')
    return com_https, termina_com_br

url = "https://www.gov.br"
tem_https, tem_br = analisar_url(url)
print(f'utiliza https? {tem_https}')
print(f'termina com .br? {tem_br}')

# verificar se a string contem somente números
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print('o valor digitado é uma idade valida!')
    else:
        print('digite somente numeros!')

idade = input('digite sua idade: ')
validar_idade(idade)

#verificar se a string contem somente letras
def validar_nome(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
        print('o nome digitado é valido!')
    else:
        print('digite somente letras!')

nome = input('digite um nome valido: ')
validar_nome(nome)
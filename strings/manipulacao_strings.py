# converter texto para maiusculas e minusculas
def formatar_nome(nome):
    nome_maiusculo = nome.upper()
    nome_minusculo = nome.lower()

    #nome com a primeira letra maiuscula
    nome_camel_case = nome_maiusculo.capitalize()

    return (nome_maiusculo, nome_minusculo, nome_camel_case)

nome = input('digite seu nome: ')

# print(formatar_nome(nome)[0])

banana, batata, cebola = formatar_nome(nome)
print(f'nome maiusculo: {banana}')
print(f'nome minusculo: {batata}')
print(f'nome camel case: {cebola}')

# remover espaços desnecessarios
def limpar_texto(texto):
    texto_limpo = texto.strip()
    return texto_limpo

texto1 = '    Aprender python é legal!!      '
print(f'texto antes: {texto1}')
print(f'texto depois: {limpar_texto(texto1)}')

# substituir palavras
def trocar_cidade(texto):
    texto_trocado = texto.replace(cidade, "piracicaba")
    return texto_trocado


cidade = input('digite sua cidade: ')
print(f'eu moro em: {trocar_cidade(cidade)}')

# contar caracteres ou ocorrencias
def analisar_texto(texto):
    qtde_caracteres= len(texto)

# contar a quantidade de ocorrencia
    qtde_letras = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letras

texto_2 = input('digite seu texto: ')
letra = input('digite uma letra: ')
caracteres, letras = analisar_texto(texto_2, letra)

print(f'caracteres: {caracteres}')
print(f'total de letras : {letras}')

# verificar se uma palavra esta presente
def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    # retorna um booleano (true ou false)
    return palavra_presente

frase = input('digite uma frase: ')
palavra = input('digite uma palavra: ')

print(f'a palavra esta presente na frase? {verificar_palavra(frase, palavra)}')

# encontrar a posição de uma palavra
def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower)
    return posicao_palavra

frase_2 = input('digite uma nova frase: ')
palavra2 = input('digite uma palavra para saber sua posição: ')

print(f'a posição da palavra é {encontrar_posicao_palavra(frase_2, palavra2)}')
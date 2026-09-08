def validar_telefone(numeros):
    numero_valido = numeros.isdigit()

    if numero_valido:
        print('Número de telefone válido!')
    else:
        print('Número inválido! Digite somente números.')

numeros = input('digite seu número de telefone: ')

validar_telefone(numeros)
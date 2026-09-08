def validar_senha(senha):
    tamanho = len(senha)
    tem_letra = False
    tem_numero = False
    tem_espaco = False

    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere.isspace():
            tem_espaco = True

    if tamanho >= 8 and tem_letra and tem_numero and tem_espaco == False:
        print('Senha válida!')
    else:
        print('Senha inválida!')


senha = input('digite sua senha: ')
validar_senha(senha)
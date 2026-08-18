def alunoaprovado():
    nota_1 = int(input('Qual a primeira nota: '))
    nota_2 = int(input('Qual a segunda nota: '))

    media = (nota_1 + nota_2) / 2

    if media >= 6:
        print('Aluno aprovado!')
    elif media >= 5 and media < 6:
        print('Aluno de Recuperação!')
    else:
        print('Aluno reprovado!')


#alunoaprovado()

def login():
        email = 'manuu@gmail.com'
        senha = '1234'
        codigo_secreto = '#456@'

        email_input = input('Digite o seu email:')
        senha_input = input('Digite sua senha:')

        if email_input == email and senha_input == senha:
            print('usuario logado!')
            acessar_admin = input('Deseja acessar area administrativa? (S/N)')
            if acessar_admin == 'S':
               codigo_secreto_input = input('Digite o seu codigo secreto')
               if codigo_secreto_input == codigo_secreto:
                   print('acesso ADM liberado!')
               else:
                   print('codigo secreto incorreto!')
            elif acessar_admin == 'N':
                print('ok, voce acessou como usuario comum!')
            else:
                print('opcao invalida!')

        else:
            print('e-mail ou senha incorreto!')

login()
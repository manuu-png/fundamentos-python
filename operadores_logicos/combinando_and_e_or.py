# operadores and e or
from operator import truediv


def posso_entrar_no_show_do_veigh():
    POSSUI_INGRESSO = True
    idade = int(input('Digite a idade: '))
    nome_esta_na_lista = bool(input('Sua nome está na lista? '))

    posso_entrar = (nome_esta_na_lista or POSSUI_INGRESSO) and idade >= 18

    print(f'vou conseguir entrar no show? {posso_entrar}')

posso_entrar_no_show_do_veigh()
def numero():
    inteiro = int(input('digite um numero inteiro: '))
    antecessor = inteiro - 1
    sucessor = inteiro + 1
    print(f'o antecessor e sucessor de {inteiro} é {antecessor} , {sucessor}')
    return inteiro, antecessor, sucessor

numero()


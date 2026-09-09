from calculadora import *

def executar_calculadora():
    operacoes = {
        '1': somar,
        '2': subtrair,
        '3': multiplicar,
        '4': dividir
    }

    while True:
        print("===========CALCULADORA===========\n")
        print('------ESCOLHA UMA OPÇÃO-----*\n')
        print('[1] Somar')
        print('[2] Subtrair')
        print('[3] Multiplicar')
        print('[4] Dividir')
        print('[0] Sair')

        opcao = input('escolha uma opção: ')

        if opcao == '0':
            print('-----CALCULADORA ENCERRADA-----')
            break

        if opcao not in operacoes:
            print("opção invalida!")
            continue

        numero1 = float(input('digite o primeiro numero: '))
        numero2 = float(input('digite o segundo numero: '))

        funcao = operacoes[opcao]

        resultado = funcao(numero1, numero2)

        print(f'o resultado é {resultado}')

executar_calculadora()
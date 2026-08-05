def exibir_mensagem():
    print('hello world!!')


def somar():
    valor1 = 50
    valor2 = 60
    total = valor1 + valor2
    print(f'o resultado da soma é {total}')

def calcularmedia():
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    return media

exibir_mensagem()
somar()

nota_final = calcularmedia()
print(f'a nota final foi {nota_final}')

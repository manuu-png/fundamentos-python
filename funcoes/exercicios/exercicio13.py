def comissao():
    salario = float(input('Digite seu salario: '))
    vendas = float(input('Digite o valor de vendas: '))
    percentual = vendas / salario * 100
    print(f'O percentual das vendas foi de {percentual:.2f}%')
    return percentual

comissao()
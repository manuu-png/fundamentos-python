def calcularsalario():
    valor_hora = float(input('Digite o valor da hora: '))
    hora_trabalhada = float(input('Digite a hora trabalhada: '))
    salario = valor_hora * hora_trabalhada
    print(f'O seu salario é de {salario:.2f} reais')
    return salario

calcularsalario()

def contas():
    base = int(input("Digite o valor base: "))
    altura = int(input("Digite o valor altura: "))
    perimetro =  2 * (base + altura)
    print(f'o valor do perimetro é de {perimetro}')
    return perimetro

contas()
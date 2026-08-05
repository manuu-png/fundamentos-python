def calculo():
    base = int(input("Digite o valor base: "))
    altura = int(input("Digite o valor altura: "))
    area = base * altura
    print(f'base: {base} X altura: {altura} = area: {area}')
    return area

calculo()
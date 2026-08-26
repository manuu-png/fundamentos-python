def quantidade_elementos(lista):
    quantidade = len(lista)
    print(f'a quantidade de frutas da lista é {quantidade}')
    return quantidade


frutas = []

quantidade = int(input('quantas frutas deseja adicionar? '))

for i in range(quantidade):
    fruta = input('digite o nome da fruta: ')
    frutas.append(fruta)

quantidade_elementos(frutas)
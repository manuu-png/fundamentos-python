def inverter_lista(lista):
    lista_invertida = list(reversed(lista))
    print(f'a lista invertida é {lista_invertida}')
    return lista_invertida


lista = []

quantidade = int(input('quantos elementos deseja adicionar? '))

for i in range(quantidade):
    elemento = input('digite um elemento: ')
    lista.append(elemento)

inverter_lista(lista)
def adicionar_cliente(fila, cliente):
    fila.append(cliente)
    print(f'o cliente {cliente} entrou na fila: {fila}')


def atender_cliente(fila):
    cliente = fila.pop(0)
    print(f'o cliente atendido foi {cliente}')
    return cliente


fila = []

while True:
    cliente = input('digite o nome do cliente ou "sair": ')

    if cliente == 'sair':
        break
    else:
        adicionar_cliente(fila, cliente)

print(f'a fila final é: {fila}')

if len(fila) > 0:
    atender_cliente(fila)
    print(f'a fila atualizada é: {fila}')
else:
    print('não existem clientes na fila')
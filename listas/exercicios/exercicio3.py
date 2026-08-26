def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(f'os novos convidados {novos_convidados} foram adicionados à lista: {convidados}')


convidados = []

novos_convidados = []

quantidade = int(input('quantos convidados deseja adicionar? '))

for i in range(quantidade):
    nome = input('digite o nome do convidado: ')
    novos_convidados.append(nome)

adicionar_convidados(convidados, novos_convidados)
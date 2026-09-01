def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    temperaturas_ordenadas = sorted(temperaturas)

    print(f'a quantidade de temperaturas é {quantidade}')
    print(f'a soma das temperaturas é {soma}')
    print(f'a média das temperaturas é {media}')
    print(f'as temperaturas ordenadas são {temperaturas_ordenadas}')

    return quantidade, soma, media, temperaturas_ordenadas


temperaturas = []

quantidade = int(input('quantas temperaturas deseja adicionar? '))

for i in range(quantidade):
    temperatura = float(input('digite uma temperatura: '))
    temperaturas.append(temperatura)

analisar_temperaturas(temperaturas)
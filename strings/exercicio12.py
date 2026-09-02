def separar_dados(dados):
    partes = dados.split(',')

    print(f'Nome: {partes[0]}')
    print(f'Idade: {partes[1]}')
    print(f'Profissão: {partes[2]}')
    print(f'Cidade: {partes[3]}')

dados = "João,40,Desenvolvedor,Piracicaba"

separar_dados(dados)
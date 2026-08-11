def cadastro():
    nome = input('Qual o seu nome?')
    idade = int(input('Qual a sua idade?'))
    profissao = input('Qual o seu profissao?')
    cidade = input('Qual a sua cidade?')

    print(f'--- Cadastro ---')
    print(f'Nome: {nome}')
    print(f'Idade: {idade} anos')
    print(f'Profissao: {profissao}')
    print(f'Cidade: {cidade}')

cadastro()
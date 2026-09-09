# anatomia do dicionario

import json

def exibir_alunos():
    alunos = {
        'nome': 'manu',
        'idade': 17,
        'curso': 'desenvolvimento de sistemas'
    }

    print('alunos:', alunos['nome'])
    print('idade:', alunos['idade'])
    print('curso:', alunos['curso'])
    print('notas:', alunos.get('notas'))


#exibir_alunos()

def atualizar_idade():
    alunos = {
        'nome': 'manu',
        'idade': 17,
        'curso': 'desenvolvimento de sistemas'
    }

    print('idade antes: ', alunos.get('idade'))
    alunos['idade'] = 18
    print('idade depois: ', alunos.get('idade'))

#atualizar_idade()

# adicionando novas informações
def adicionar_informacao():
    aluno = {
        'nome': 'maria',
        'idade': 19
    }
    print('alunos antes: ', aluno)
    aluno['curso'] = 'tecnica automotiva'
    aluno['notas'] = 2
    print('alunos depois: ', aluno)

#adiciona_informacao()

def verificar_chave():
    aluno = {
        'nome': 'camila',
        'idade': 18
    }

    if 'nome' in aluno:
        print('o nome esta cadastrado')

    if 'notas' not in aluno:
        print('a notas nao esta cadastrado')

#verificar_chave()

# utilizando comparações
def verificar_aprovacao():
    aluno = {
        'nome': 'manu',
        'idade': 17,
        'curso': 'desenvolvimento de sistemas',
        'nota': 6.5,
        'frequencia': 90
    }

    if aluno['nota'] >= 6 and aluno['nota'] >= 75:
        print(f'o aluno {aluno["nome"]} esta aprovado')
    else:
        print(f'o aluno {aluno['nome']} nao foi aprovado')

#verificar_chave()
def listar_campos():
    produto = {
        'nome': 'caneta',
        'quantidade': 17,
        'preco_unitario': 1.25
    }

    for chave in produto.keys():
        print(chave)

#listar_campos()
def listar_valores():
    produto = {
        'nome': 'caneta',
        'quantidade': 17,
        'preco_unitario': 1.25
    }

    for valor in produto.values():
        print(valor)

#listar_valores()

def exibir_produto():
    produto = {
        'nome': 'caneta',
        'quantidade': 17,
        'preco_unitario': 1.25
    }

    for chave, valor in produto.items():
        print(f'a chave: {chave} valor: {valor}')

#exibir_produto()

def atualizar_estoque():
    produto = {
        'nome': 'caneta',
        'quantidade': 17,
        'preco_unitario': 1.25
    }

    produto['total'] = produto['quantidade'] * produto['preco_unitario']
    print(produto)

#atualizar_estoque()
def remover_informacao():
    produto = {
        'nome': 'caneta',
        'quantidade': 17,
        'preco_unitario': 1.25
    }


    del produto['nome']
    print(produto)

    preco_unitaria = produto.pop('preco_unitario')
    print(produto, preco_unitaria)


#remover_informacao()
def listar_produtos():
    produtos = [
        {'nome': 'teclado', 'preco': 299.00, 'quantidade': 2},
        {'nome': 'mouse', 'preco': 25.00, 'quantidade': 3},
        {'nome': 'monitor', 'preco': 1200.00, 'quantidade': 1},
    ]
    total_geral = 0
    for produto in produtos:
        print(f'o produto {produto["nome"]} custa {produto["preco"]}')
        total_individual = produto['preco'] * produto['quantidade']
        total_geral += total_individual
        print(total_individual)

        print(f'total geral: {total_geral}')

#listar_produtos()

def cadastrar_aluno():
    aluno = {}

    aluno['nome'] = input('informe o nome do aluno: ')
    aluno['idade'] = int(input('informe a idade: '))
    aluno['curso'] = float(input('informe o curso: '))
    aluno['email'] = float(input('informe o email: '))

    print(f'dados castrados! novo aluno: {aluno}')

#cadastrar_aluno()

def criar_cadastro():
    dados = {}

    quantidade = int(input('quantos dados vc deseja cadastrar? : '))

    for itens in range(1, quantidade + 1):
        chave = input(f'digite o nome do campo: ')
        valor = input(f'digite o valor de {chave}: ')

        dados[chave] = valor

    print('cadastro final: ', dados)

#criar_cadastro()

# dicionario com listas
def calcular_media(notas):
    return sum(notas) / len(notas)


def aluno_completo():
    aluno = {
        'nome': 'manu',
        'idade': 17,
        'curso': 'desenvolvimento de sistemas',
        'notas': [7.8, 6.7, 10, 5.9],
        'endereco': {
            'cidade': 'piracicaba',
            'rua': 'joao batista',
            'numero': 1267,
            'telefone': '(19) 98845-3689'
        }
    }
    aluno['media'] = calcular_media(aluno['notas'])
    print(aluno["endereco"]["telefone"])

#aluno_completo()

def cadastrar_dados_alunos():
    aluno = {}

    aluno['nome'] = input('informe o nome do aluno: ')
    aluno['idade'] = int(input('informe a idade: '))
    aluno['notas'] = []

    for nota in range(4):
        aluno['nota'].append(float(input(f'informe a nota {nota + 1}: ')))

    aluno['endereco'] = {}
    aluno['endereco']['cidade'] = input('digite a cidade: ')
    aluno['endereco']['rua'] = input('digite a rua: ')
    aluno['endereco']['numero'] = int(input('digite o numero da casa: '))
    aluno['endereco']['telefone'] = input('digite o telefone com DDD: ')

    aluno['media'] = calcular_media(aluno['notas'])
    print('aluno cadastrado: ', json.dumps(aluno, indent=4))

cadastrar_dados_alunos()


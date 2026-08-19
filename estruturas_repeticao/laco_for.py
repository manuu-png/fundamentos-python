# Laço for simples
import time

def mostrar_numero():
    for i in range(1,6):
        print(f'o numero atual é {i}')
        time.sleep(5)

#mostrar_numero()

def mostrar_numero_alternado():
    for num in range(0,20, 2):
        print(f'o numero atual é {num}')

#mostrar_numero_alternado()

def somar_numero():
    total = 0
    for valor in range(1,20):
        total += valor
        print(total)

#somar_numero()

def mostrar_numeros_pares():
    for numero in range(1,21):
        if numero % 2 !== 0:
            print(f'numeros pares: {numero}')

#mostrar_numero()

def mostrar_item_da_lista():
    sacola_de_frutas = ['maçã', 'morango', 'banana', 'framboesa']
    for sacola in sacola_de_frutas:
        print(f'na minha sacola contem {sacola}')

#mostrar_item_da_lista()
def laco_aninhado():
        nome = ['Manu', 'Camila', 'Luiza e Maria']
        notas = [8, 9, 10]
        for nome in nome:
            print(f'nome dos alunos: {nome}')
            for nota in notas:
                print(f'nota dos alunos: {nota}')
laco_aninhado()
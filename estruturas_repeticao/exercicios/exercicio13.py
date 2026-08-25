from estruturas_repeticao.exercicios.exercicio12 import eh_primo


def mostrar_primos(inicio, fim):
    print(f"Números primos entre {inicio} e {fim}:")
    for numero in range(inicio, fim + 1):
        if eh_primo(numero):
            print(numero)

inicio1 = int(input("Digite o início : "))
fim1 = int(input("Digite o fim: "))
mostrar_primos(inicio1, fim1)
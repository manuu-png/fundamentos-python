def verificar():
    numero = int(input("digite um numero inteiro: "))

    if numero > 0:
        print(f"o numero é positivo")
    elif numero < 0:
        print(f"o numero é negativo")
    else:
        print(f"numero é zero")

verificar()
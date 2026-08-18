def maior():
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))

    if num1 > num2:
        print(f"o maior número é {num1}")
    elif num2 > num1:
        print(f"o maior número é {num2}")
    else:
        print(f"os números são iguais")


maior()
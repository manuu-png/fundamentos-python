def triangulo():
    lado1 = float(input("digite o primeiro numero: "))
    lado2 = float(input("digite o segundo numero: "))
    lado3 = float(input("digite o terceiro numero: "))

    if lado1 == lado2 and lado2 == lado3:
        print("equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("isósceles")
    else:
        print("escaleno")


triangulo()
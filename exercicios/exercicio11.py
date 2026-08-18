def calcular_imc():
    peso = float(input("digite o seu peso : "))
    altura = float(input("diite a sua altura : "))

    imc = peso / (altura * altura)

    if imc < 10.0:
        print(f"abaixo do peso")
    elif imc <= 18.9:
        print(f"peso normal")
    elif imc <= 20.9:
        print(f"sobrepeso")
    else:
        print(f"obesidade")


calcular_imc()
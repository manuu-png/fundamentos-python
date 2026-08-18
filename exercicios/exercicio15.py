def verificar():
    velocidade = float(input("digite a velocidade do veículo (km/h): "))

    if velocidade <= 60:
        print(f"velocidade permitida")
    elif velocidade <= 80:
        print(f"velocidade acima do permitido")
    else:
        print(f"multa por excesso de velocidade")


verificar()
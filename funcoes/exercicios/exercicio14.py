def combustivel():
    distancia = float(input('Digite a distancia percorrida: '))
    quantidade = float(input('Digite a quantidade de combustivel: '))

    consumo = distancia / quantidade
    print(f'O consumo medio é de {consumo} km/L')
    return consumo

combustivel()
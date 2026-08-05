def calculo():
    temperatura = float(input('Digite a temperatura em graus Celsius: '))
    fahrenheit = temperatura * 1.8 + 32
    print(f"a temperatura convertida em fahrenheit é de {fahrenheit}")
    return fahrenheit

calculo()
    
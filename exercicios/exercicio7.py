def temperatura():
    celsius =float(input("digite a temperatura em graus Celsius: "))

    if celsius > 15:
        print(f"frio")
    elif celsius <= 25:
        print(f"agradavel")
    else:
        print(f"quente")
temperatura()
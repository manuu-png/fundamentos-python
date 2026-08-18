def classificar():
    nota = float(input("digite sua nota : "))

    if nota <= 4:
        print(f"insuficiente")
    elif nota <=6:
        print(f"regular")
    elif nota <=8:
        print(f"bom")
    else:
        print(f"excelente")

classificar()
def saque():
    saldo = float(input("digite o saldo: "))
    valor = float(input("digite o valor do saque: "))

    if valor > saldo:
        print("saldo insuficiente")
    elif valor <= 0:
        print("valor de saque inválido")
    else:
        saldo = saldo - valor
        print("Saque realizado com sucesso")
        print("Novo saldo é de : {saldo}")


saque()
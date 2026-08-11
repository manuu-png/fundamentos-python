def conversao():
    idade = int(input("Qual a sua idade?"))

    meses = idade * 12
    dias = idade * 365
    print(f'vc tem {idade} anos, {meses} meses e {dias} dias')
    return idade, meses, dias

conversao()

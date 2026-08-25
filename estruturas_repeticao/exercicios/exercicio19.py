def menu():
    while True:
        print("\n1 - números de 1 a 10")
        print("2 - números pares")
        print("3 - tabuada")
        print("4 - sair")

        opcao = input("escolha uma opção: ")

        if opcao == "1":
            for i in range(1, 11):
                print(i)

        elif opcao == "2":
            for i in range(2, 11, 2):
                print(i)

        elif opcao == "3":
            numero = int(input("digite um número: "))

            for i in range(1, 11):
                print(numero, "x", i, "=", numero * i)

        elif opcao == "4":
            print("Programa encerrado")
            break

        else:
            print("Opção inválida")


menu()

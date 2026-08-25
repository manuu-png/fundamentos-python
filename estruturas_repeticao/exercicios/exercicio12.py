def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

num2 = int(input("Digite um número: "))
if eh_primo(num2):
    print(f"O número {num2} é primo!")
else:
    print(f"O número {num2} não é primo.")
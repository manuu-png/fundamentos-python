def aprovacao():
    nota = float(input("digite a nota do aluno : "))

    if nota >= 6:
        print(f"aprovado")
    else:
        print(f"reprovado")

aprovacao()
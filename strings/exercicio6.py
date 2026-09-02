def contar_letra(frase, letra):
    quantidade = frase.lower().count(letra.lower())
    return quantidade

frase = input('digite uma frase: ')
letra = input('digite uma letra: ')

print(f'a letra aparece {contar_letra(frase, letra)} vezes')
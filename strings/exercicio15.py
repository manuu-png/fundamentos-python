def validar_especie(animal):
    animal_valido = animal.isalpha()

    if animal_valido:
        print('Espécie de animal válida.')
    else:
        print('Espécie inválida.')

animal = input('digite uma espécie de animal: ')

validar_especie(animal)

# A sintaxe lista_numeros[:] é usada para criar uma cópia de uma lista em Python. Isso é conhecido como uma cópia superficial, pois cria uma nova lista que contém os mesmos elementos que a lista original. No entanto, se a lista original contiver objetos mutáveis, como outras listas ou dicionários, as alterações nesses objetos também serão refletidas na lista clonada

lista_numeros = [1, 2, 3, 4, 5]
lista_clonada = lista_numeros[:]

lista_clonada += [6]  # Resultado: [1, 2, 3, 4, 5, 6]
print(lista_numeros)

print(lista_clonada)  # Resultado: [1, 2, 3, 4, 5, 6]
lista_numeros += [7]

print(lista_numeros)  # Resultado: [1, 2, 3, 4, 5, 6, 7]
print(lista_clonada)  # Resultado: [1, 2, 3, 4, 5, 6]


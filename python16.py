
# Enumerate the items of the supermaket with indice and indice with sorting method

itens = [ "meat", "egg", "sausage", "carrot"]

for indice, items in enumerate(itens,1):
  print(indice,items)

itens.sort() # Deixar ordenado
for indice, items in enumerate(itens):
  print(indice+1, items)

lista_numeros = [1,2,3,4,5]
nova_lista = lista_numeros 

print(lista_numeros) # Resultado: [1,2,3,4,5]
print(nova_lista)    # Resultado: [1,2,3,4,5]

lista_numeros += [6]
print(lista_numeros) # Resultado: [1,2,3,4,5,6]
print(nova_lista)    # Resultado: [1,2,3,4,5,6]

nova_lista += [7]
print(lista_numeros) # Resultado: [1,2,3,4,5,6,7]
print(nova_lista)    # Resultado: [1,2,3,4,5,6,7]



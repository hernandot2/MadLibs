
# Enumerate the items of the supermaket with indice and indice with sorting method

itens = [ "meat", "egg", "sausage", "carrot"]

for indice, items in enumerate(itens,1):
  print(indice,items)

itens.sort() # Deixar ordenado
for indice, items in enumerate(itens):
  print(indice+1, items)










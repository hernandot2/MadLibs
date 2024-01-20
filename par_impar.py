lista_pares = []
lista_impares = []

while True:
  numero = int(input("Digite algum numero( Digite zero para encerrar):"))
  if numero == 0:
    break
  if numero % 2 == 0:
    lista_pares.append(numero)
  else:
    lista_impares.append(numero)

lista_pares.sort()
lista_impares.sort()

print(lista_pares)
print(lista_impares)

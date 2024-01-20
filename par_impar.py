lista_pares = []
lista_impares = []
while True:
  numero = int(input("Digitar um numero inteiro(zero para encerrar):"))
  if numero == 0:
    break
  if numero %2 == 0:
    lista_pares.append(numero)
  else:
    lista_impares.append(numero)

print(lista_pares)
print(lista_impares)
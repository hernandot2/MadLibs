

list_even = [ ]
list_odd = [ ]

while True:
  numero = int(input(" Inform a integer number and zero to stop: "))
  if numero == 0:
    break
  if numero % 2 == 0:
    list_even.append(numero)
  else:
    list_odd.append(numero)

  list_even.sort()
  list_odd.sort()

  print(f"There are {list_even} even")
  print(f"There are {list_odd} odd")
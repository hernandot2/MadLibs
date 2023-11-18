
# Este código em Python é usado para separar números pares e ímpares em duas listas diferentes. O código começa criando duas listas vazias, uma para números pares e outra para números ímpares. Em seguida, ele entra em um loop infinito que solicita ao usuário que insira um número inteiro. Se o número for zero, o loop é interrompido. Se o número for par, ele é adicionado à lista de números pares. Se for ímpar, é adicionado à lista de números ímpares. As duas listas são então classificadas em ordem crescente e o número de elementos em cada lista é impresso. Por exemplo, se o usuário inserir os números 3, 6, 2, 1 e 4, o programa imprimirá "Existem [2, 4, 6] números pares" e "Existem [1, 3] números ímpares". Espero que isso ajude! 😊


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
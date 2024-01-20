# lista = [] 
# while True:
#   numero = int(input("Digite um numero inteiro(0 para sair):"))
#   if numero == 0:
#     break 
#   lista.append(numero) 


lista = [] # comeca-se com uma lista vazia 
while True:
  numero = int(input("Digite um numero inteiro(zero p sair):")) # ai quando adiciona um numero vai para o list.append(numero)

  if numero == 0: # se o numero informado for zero 
    break
  lista.append(numero)
print(numero)

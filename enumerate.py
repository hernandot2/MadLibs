estacoes = ["verao", "inverno", "outono"]
lista_estacoes = list(enumerate(estacoes))
print(lista_estacoes)

lista_estacoes = list(enumerate(estacoes, start = 5))
print(lista_estacoes)

#enumerate com for

itens = ["carne", "porco", "frango", "salsicha"]
for indice, x in enumerate(itens,1):
    print(indice,x)

itens.sort()
for indice, x in enumerate(itens):
    print(indice+1,x)
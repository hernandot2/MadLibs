# Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero. Adicione os números informados em uma lista e, ao final do programa, imprima a soma de todos os números, a multiplicação de todos os números, o maior e o menor número informado.



# a = int(input("Informe o valor de 'a': "))
# b = int(input("Informe o valor de 'b': "))
# print(f"a é maior que b: {a>b}")
# print(f"a é menor que b: {a<b}")
# print(f"a é igual a b: {a==b}")





# Exemplo de execução:

# Informe um número (zero para sair): 10

# Informe um número (zero para sair): 5

# Informe um número (zero para sair): 20

# Informe um número (zero para sair): 0

 

# Soma: 35

# Multiplicação: 1000

# Maior número: 20

# Menor número: 5




#Estruturas de dados - Listas
# Criando uma lista com 3 inteiros
lista_numeros = [25, 78, 55]
# Será impresso 78, os elemetos da lista iniciam com zero
# 0=25, 1=78, 2=55
# Na linha abaixo será impresso 78
print(lista_numeros[1])


# Acessando os elementos para calcular a média
notas = [7.5, 5.6, 9.5, 10.0]
media = (notas[0] + notas[1] + notas[2] + notas[3])/4
print(media)

bancos = ["Banco do Brasil", "CEF", "Banestes"]
print(bancos)

bancos[0] = "banco do japao"
print(bancos)


#Para incrementar o valor de uma lista podemos usar o operador de adição.
numeros = [1, 2, 3, 10, 12]
numeros = numeros + [8, 7, 15]
print(numeros)


# insert

banco = [ 1, 2, 3]
banco.insert (0,5)
print(banco)




# Interpolacao
valor_unitario = 165.78
quantidade = 5 
valor_total = valor_unitario * quantidade 
frase = "O produto custa %f. Eu comprei %d. Paguei ao todo %f" % ( valor_unitario, quantidade, valor_total)
print(frase)


valor_unitario = 165.78
quantidade = 5 
valor_total = valor_unitario * quantidade 
frase = f"O produto custa {valor_unitario}. Eu comprei {quantidade}. Paguei ao todo {valor_unitario * quantidade}"
print(frase)


# Crie um programa que possua duas variáveis denominadas nome e sobrenome.
# Solicite que o usuário informe o nome e depois solicite que informe o sobrenome e grave nas variáveis separadamente.
# Crie uma variável denominada nome_completo e grave o nome e sobrenome concatenados.
# No final do programa imprima a frase:
# Seu nome completo é: NOME SOBRENOME
# Onde NOME e SOBRENOME é o conteúdo da variável nome_completo.


nome = input("nome:")
sobrenome =  input("sobrenome:")
nome_completo = nome +" " +sobrenome
frase = f"Seu nome completo é: {nome_completo}"
print(frase)


# Crie um programa que solicite uma palavra ao usuário e armazene
# esta palavra em uma variável denominada 'palavra'.
# Em seguida imprima o conteúdo da variável 20 vezes usando a multiplicação de strings.
# Lembre-se de colocar um espaço para não imprimir as palavras "coladas".

palavra = input("Informe uma palavra: ")
print((palavra + ' ') * 20)
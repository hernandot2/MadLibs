texto1 = "ola"
texto2 = " tudo bem?"

soma_dos_textos = texto1 + texto2
print(soma_dos_textos)


pao = " paozinho"
multiplicacao = pao * 10 
print(multiplicacao)



nome = "joao"
idade = 28
filhos = 2

frase = "O jogador %s tem %d anos e %d filhos " %(nome, idade, filhos)
print(frase)

aula = 9
print(" esta eh a aula %03d" % aula)

nome = "joao"
idade = 28
filhos = 5
frase = " o jogador {} tem {} anos e {} filhos." .format( nome, idade, filhos)

print(frase) 
texto1 = "ola"
texto2 = " tudo bem?"

soma_dos_textos = texto1 + texto2
print(soma_dos_textos)


pao = " paozinho"
multiplicacao = pao * 10 
print(multiplicacao)


nome = "joao"
idade = 9
filhos = 2 

frase = " o jogador %s tem %d anos e  tem %d filhos " %(nome, idade, filhos)
print(frase)

aula = 9
print(" esta eh a aula %03d" % aula)

nome = "joao"
idade = 28
filhos = 5
frase = " o jogador {} tem {} anos e {} filhos." .format( nome, idade, filhos)

print(frase) 


frase = " ola, eu vou viajar de {0}" .format('busao', 'bicicleta', 'carro')
print(frase)
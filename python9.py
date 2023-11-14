
# Fazer um programinha de soma, que as pessoas informem os numeros inteiros, e
# que possam informar a quantidade de numeros para soma. 
# Para isso, tem que ter variaveis de somar, qtd de numero e while para ter continuidade
# da operacao. e uma condicao que de END quando a pessoa coloca o numero negativo como quantidade

soma = 0 # soma os numeros
x = 0 # executa a operacao de somar
qtd_numeros = int(input(" Informe a qtd de numeros p/ somar:"))

while x < qtd_numeros:
  x = x + 1
  soma = soma + int(input(" Informe um numero inteiro: "))

else:
   print(f"Soma:{soma}")
   print("acabou")


while True:
    x = input("Informe o valor de x: ")
    z = x + x
 
print(z)
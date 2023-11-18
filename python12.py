# Faça um programa que solicite ao usuário um número que ele
# queira treinar a tabuada. Você irá solicitar ao mesmo a resposta
# do cálculo do número informado multiplicado por 1, 2, até 10. A
# cada resposta você deverá validar e imprimir: “Correto” ou “Que
# pena, você errou, o valor correto é x”, no lugar de “x” coloque o
# valor correto. Ao final imprima “Total de acertos: y” e “Total de
# erros: z”, onde “y” deverá ser o total de acertos e “z” o total de
# erros.

# Aqui esta pedindo o numero para tabuada. Depois de pedir o numero para calcular
# a pessoa tem que responder essa tabuada escolhida de 1 a 10. 
# Portanto tera que ter uma variavel numero e depois vai respondendo os numeros, se errar
# a conta numero * n , aparecera mensagem de que errou e se acertou aparecera que acertou,
# para isso tem q ter mais uma variavel para igualar no 'if ==' quando acerta e quando erra.
# Ainda tem ter mais duas variaveis para contabilizar os acertos e erros. 

# phrase = f"O valor da compra eh: {valor_total:,.2f} "
    # Solicitar ao usuario um numero para a tabuada

numero = int(input("Digite um número para treinar a tabuada: "))

acertos = 0
erros = 0

for n in range(1, 11):
    resposta = int(input(f"{numero} * {n}? "))
    if resposta == (numero * n):
        print("Resposta correta")
        acertos += 1
    else:
        print(f"Que pena você errou, a resposta correta é {numero * n}")
        erros += 1

# Os prints finais devem estar fora do loop
print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")

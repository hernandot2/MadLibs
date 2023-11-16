# Faça um programa que solicite ao usuário um número que ele
# queira treinar a tabuada. Você irá solicitar ao mesmo a resposta
# do cálculo do número informado multiplicado por 1, 2, até 10. A
# cada resposta você deverá validar e imprimir: “Correto” ou “Que
# pena, você errou, o valor correto é x”, no lugar de “x” coloque o
# valor correto. Ao final imprima “Total de acertos: y” e “Total de
# erros: z”, onde “y” deverá ser o total de acertos e “z” o total de
# erros.

def main():
    # Solicitar ao usuário um número para a tabuada
    numero = int(input("Digite um número para treinar a tabuada: "))

    acertos = 0
    erros = 0

    # Loop de 1 a 10 para a tabuada
    for i in range(1, 11):
        resposta_usuario = int(input(f"Qual é {numero} x {i}? "))
        resposta_correta = numero * i

        # Verificar se a resposta está correta
        if resposta_usuario == resposta_correta:
            print("Correto")
            acertos += 1
        else:
            print(f"Que pena, você errou, o valor correto é {resposta_correta}")
            erros += 1

    # Imprimir o total de acertos e erros
    print(f"Total de acertos: {acertos}")
    print(f"Total de erros: {erros}")

if __name__ == "__main__":
    main()

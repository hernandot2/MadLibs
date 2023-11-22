
# Write a program that requests several numbers from the user, one at a time, 
# making it possible to end data entry by entering zero. Add the numbers entered into a list and, at the end of the program, print the sum of all numbers, the multiplication of all numbers, the largest and smallest numbers entered.
list_even = []  # Inicializa a lista de números pares
list_odd = []   # Inicializa a lista de números ímpares

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





def main():
    numbers = [] # Lista numbers Dentro da função main(), primeiro criamos uma lista vazia chamada numbers. Esta lista é usada para armazenar todos os números que o usuário digita.
    while True: # Loop while True Depois, temos um loop while True, que continua rodando até que seja interrompido por um break. Isso significa que ele vai continuar pedindo números ao usuário até que o usuário digite 0.
        try: # Bloco try-except Dentro do loop, temos um bloco try-except: try: Aqui, o programa tenta converter a entrada do usuário para um número decimal (float) e verifica se esse número é 0. Se for 0, o comando break interrompe o loop. Se não for 0, o número é adicionado à lista numbers.

            number = float(input("Enter a number (or 0 to finish): "))
            if number == 0:
                break
            numbers.append(number)
            
# except ValueError: Se o usuário digitar algo que não possa ser convertido em um número (como letras ou símbolos), o Python irá gerar um erro chamado ValueError. O bloco except captura esse erro e imprime uma mensagem pedindo para o usuário digitar um número válido.
# Cálculo e Impressão dos Resultados
# if numbers:: Esta linha verifica se a lista numbers não está vazia (ou seja, o usuário digitou pelo menos um número diferente de 0).

        except ValueError:
            print("Please enter a valid number.")

    if numbers:
        sum_of_numbers = sum(numbers) # Soma: sum_of_numbers = sum(numbers) calcula a soma de todos os números na lista.
        product_of_numbers = 1
        for num in numbers:
            product_of_numbers = product_of_numbers * num
        max_number = max(numbers)
        min_number = min(numbers)

        print(f"Sum of all numbers: {sum_of_numbers}")
        print(f"Product of all numbers: {product_of_numbers}")
        print(f"Largest number entered: {max_number}")
        print(f"Smallest number entered: {min_number}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()



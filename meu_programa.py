valor_fixo = 45
resposta =int( input("Informe um numero de 1 a 10: "))
soma = valor_fixo + resposta
print(resposta)

# Create a program that requests the user's full name and prints "Thank you for answering the question so-and-so", where "so-and-so" is the name provided by the user.

nome_completo = input("Informe o seu nome completo: ")
print(f"Obrigado por responder à pergunta {nome_completo}")

# Create a program that asks the user which drink they prefer with the options 1) Water, 2) Beer, 3) Wine and 4) Milk. This way:

# Requests the user's favorite drink

print("Which drink do you prefer?")
print("1)Water")
print("2)Beer")
print("3)Wine")
print("4)Milk")
option = input("Inform your number: ")

print(f"You choose the option {option}.")

#Crie um programa que solicite o ano de nascimento do usuário (com 4 dígitos) e calcule sua idade (tem que converter o ano para inteiro antes de calcular). Imprima a frase: "Você tem X anos.", onde "X" é a idade calculada.

ano_nascimento = int(input("Informe data de nascimento: "))
idade = 2023 - ano_nascimento
                        
print(f"voce tem {idade} anos")


# Create a program that asks the user to enter the value of the minimum wage (convert to float) and store it in a variable called salary_minimo, then ask the user how many salaries he would like to earn (convert to float) and store it in a variable called pretension . Print the salary value desired by the user like this:

sal_min = float(input(" Inform your salary value: "))
intention = float(input("How many salaries you would like to earn: "))
print("You intent to earn R$ ", sal_min * intention)

# Crie um programa que solicite ao usuário que informe o valor de seu salário, o valor do salário mínimo e sua idade. Compare se o valor do salário é maior que dois salários mínimos E se a idade informada é maior que 18 usando operadores lógicos e relacionais. Imprima no final: "O resultado foi X", sendo que X será "True" ou "False".

sal = float(input(" Wage value: "))
sal_min = float(input("Minimum Wage value: "))
age = int(input("How old are you: "))

x = sal > 2*sal_min and age > 18 
print("O resultado foi", x)



# Interpolacao
valor_unitario = 165.78
quantidade = 5 
valor_total = valor_unitario * quantidade 
frase = "O produto custa %f. Eu comprei %d. Paguei ao todo %f" % ( valor_unitario, quantidade, valor_total)
print(frase)

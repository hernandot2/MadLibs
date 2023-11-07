

valor_mensal = float(input("valor mensal: "))
qtd_meses = int(input( "qtd meses: "))
valor_total = qtd_meses * valor_mensal 
phrase = f"O valor da compra eh: {valor_total:,.2f} "
print(phrase)

texto1 = input("texto 1: ")
texto2 = input("texto 2: ")

print( "Texto 1:", texto1)
print( "Texto 2:", texto2)

print(f"Qtd de caracteres de {texto1}: {len(texto1)}")
print(f"Qtd de caracteres de {texto2}: {len(texto2)}")
           
print("As strings tem a mesma quantidade de caracteres?", len(texto1) == len(texto2))
print("As strings sao iguais?", texto1 == texto2)

# sal atual 
sal_atual = float(input("sal atual: "))
percentual = float(input("percentual: "))

sal_atualizado = sal_atual + ( sal_atual * ( percentual / 100))
print(f"sal atualizado eh:{salario_atualizado:,.2f}")
                  

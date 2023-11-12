

curso = "Python para todos!"
letra = ""
for x in curso:
    letra = letra + x
 
print(letra)

x = 1 # 2 a 10 
while x < 10:
    x = x + 1
    print(x)

Inicialização: x começa com o valor 1.
Entrada no Loop: O loop while verifica a condição x < 10. Na primeira iteração, como x é 1, a condição é verdadeira, então o loop prossegue.
Incremento Antes da Impressão: Dentro do loop, a primeira ação é incrementar x. Na primeira iteração, x torna-se 2 (x = x + 1).
Impressão: Depois de incrementar, o valor atual de x é impresso. Na primeira iteração, 2 é impresso.
Continuação do Loop: O loop retorna ao início. Agora x é 2. Este processo continua, incrementando x e depois imprimindo seu valor.

Última Iteração e Saída do Loop: Quando x se torna 9 e entra no loop, é incrementado para 10, e 10 é impresso. Na próxima verificação da condição do loop (while x < 10), x já é 10, então a condição é falsa, e o loop termina.

 
x = 1
while x < 10:
    print(x)
    x = x + 1
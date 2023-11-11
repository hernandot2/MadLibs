

frutas = ["gelo", "copo", "flor"]
for fruta in frutas:
    print(f"fruta:{frutas}")

else:
    print("Acabou")



for numero in range(10000):
    print(numero)
    if numero == 4:
        break
    print("Ate mais")


numeros  = [1,2,3,4,5]
for numero in numeros:
    if numero == 4:
        break
    print(f"Numero:{numero}")
else:
    print("Acabou")


for numero in range(3): # porque nao esta informando o inicio,fim,salto
    print(numero)
    

for numero in range(20, 30, 2):
    print(numero)

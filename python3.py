
# Slice
linguagens = [ "Python", "Cobol", "Clipper", "C", "C++", "Go", "JavaScript"]
linguagens2 = linguagens[3:5] # 3,4 o 5 nao eh incluido pela regra geral
print(linguagens)
print(linguagens2)

# Resultado
["Python", "Cobol", "Clipper", "C", "C++", "Go", "JavaScript"]
["C", "C++"]


letras = ['a','b','c','d','e','f','g']
print(letras)
letras[2:5] = ['C','D','E']
print(letras)
letras[2:5] = []
print(letras)
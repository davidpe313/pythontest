word=input("Escribe una palabra: ")
salida=[]
for i in range (len(word)-1,-1,-1):
    salida.append(word[i])
if list(word)==salida:
    print("Es un paplíndromo")
else:
    print("No es un palíndromo")
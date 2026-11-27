import string
abecedario = list(string.ascii_lowercase)
salida=[]
for i in range(0,len(abecedario),1):
    if i%3!=0:
        salida.append(abecedario[i])
print(salida)
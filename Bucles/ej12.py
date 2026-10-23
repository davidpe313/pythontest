phrase=input("Introduce una frase: ")
letter=input("Introduce una letras: ")
contador=0
for n in range(0,len(phrase),1):
    if phrase[n]==letter:
        contador=contador+1
print(f"La letra {letter} ha aparecido un total de {contador} veces en la frase.")
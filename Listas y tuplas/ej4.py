salida=0
lista=[]
while salida != 1:
    num=int(input("Introduce los numeros ganadores (introduce -1 para salir): "))
    if num == -1:
        salida=salida+1
    else:
        lista.append(num)
lista.sort()
print(lista)
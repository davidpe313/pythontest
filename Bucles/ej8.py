num=int(input("Introduce un numero entero: "))
salida=""
for n in range(1,num,2):
    salida=str(n)+" "+salida
    print(salida)
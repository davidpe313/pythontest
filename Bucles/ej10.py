number=int(input("Introduce un numero: "))
cantidad_divisores=0
for n in range(number,0,-1):
    if number % n ==0:
        cantidad_divisores=cantidad_divisores+1
if(cantidad_divisores==2):
    print("NUMERO PRIMO!!!!!!")
else:
    print("NUMERO NO PRIMO!!!!!!")
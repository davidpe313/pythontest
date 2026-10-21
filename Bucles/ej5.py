inversion=float(input("Introduce la cantidad a invertir: "))
interes_anual=float(input("Introduce el interes anual: "))
años=int(input("Introduce el numero de años: "))
for n in range(0,años,1):
    inversion = inversion * (1+(interes_anual/100))
    print(f"El año {n+1} has obtenido el siguiente capital: {inversion:.2f}")
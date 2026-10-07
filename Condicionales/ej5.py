edad=int(input("Introduce tu edad: "))
salario=float(input("Introduce tu salario: "))
if edad > 16 and salario >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
rent=int(input("Introduce tu renta anual: "))
if (rent<10000):
    tipo=5
elif (rent<=20000):
    tipo=15
elif (rent<=35000):
    tipo=20
elif (rent<=60000):
    tipo=30
else:
    tipo=45
print(f"Te pertenece el tipo impositivo del {tipo}")
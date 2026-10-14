score=float(input("INTRODUCE TU PUNTUACION: "))
if (score==0.0):
    print("PUNTUACION: INACEPTABLE")
elif (score==0.4):
    print("PUNTUACION: ACEPTABLE")
else:
    print("PUNTUACION: MERITORIO")
money=score*2400
print(f"HAS GANADO {money}€")

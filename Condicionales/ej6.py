gender=input("Introduce tu sexo: ")
name=input("Introduce tu nombre: ")

if gender == "f" and name < "m":
    print("Grupo A")
elif gender == "m" and name < "n":
    print("Grupo A")
else:
    print("Grupo B")
print("Tipos de pizza disponibles: vegetariana y no vegetariana")
pizza=input("Introduce el tipo de pizza: ")
if (pizza=="vegetariana"):
    print("Los ingredientes disponibles son: pimiento y tofu")
    ingredients=input("Elige un ingrediente: ")
elif (pizza=="no vegetariana"):
    print("Los ingredientes disponibles son: peperoni, jamon y salmon")
    ingredients=input("Elige un ingrediente: ")
print (f"Has elegido la pizza {pizza} con el siguiente ingrediente: {ingredients}")
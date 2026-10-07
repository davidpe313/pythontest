print("Formato admitido: 54.32")
price=input("Introduce el precio del producto: ")
# Solucion alternativa:
# pos=price.find(".")
# print(price[0:int(pos)])
# print(price[int(pos+1):len(price)])
v=price.split(".")
print(f"Numero de euros: {v[0]}€")
print(f"Numero de centimos: {v[1]} centimos")

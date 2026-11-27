list=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
final_list=[]
for i in range(0,len(list),1):
    nota=float(input(f"Introduce la nota de {list[i]}: "))
    if nota<5:
        final_list.append(list[i])
print(f"Tienes que repetir: {final_list}")
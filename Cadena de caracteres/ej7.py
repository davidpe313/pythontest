email=input("Introduce tu correo electronico: ")
find=email.find("@")
print(email[0:int(find)]+"@ceu.es")
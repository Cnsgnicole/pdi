import bcrypt
nombre = input("Ingrese su nombre: ")
contras = input("Ingrese su contraseña: ")

encriptar = contras.encode("utf-8")
sal = bcrypt.gensalt()
encript=bcrypt.hashpw(encriptar,sal)
print(encript)

user=input("Ingrese su nombre completo")

#Obtener nombre de usuario
names = user.split(" ")
username= f"{names[0][0]}{names[1]}"
print(username)
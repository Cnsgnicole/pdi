#Actividad 1
nom ="Candela Nicole Sosa Godoy"
print(nom)

#Actividad 2
num1 = int (input("Ingrese un numero: "))
num2 = int (input("Ingrese otro numero: "))

print("Suma: ", num1+num2)
print("Resta: ", num1-num2)
print("Division: ", num1/num2)
print("Multiplicacion: ", num1*num2)

#Actividad 3
edad = int(input("Ingrese su edad: "))
def mayorEdad(edad):
    if edad >= 18:
        print("Puede pasar")
    else:
        print("Vuelve a casa, para tomar una buena coca cola")
mayorEdad(edad)
#Actividad 4
listadecompras = []
final = input("Ingrese producto: ")
while final!="listo":
    listadecompras.append(final)
    final=input("Ingresar producto: ")
for i in range (len(listadecompras)):
    print(f"{i+1}. {listadecompras[i]}") 

#Actividad 5
usuarios=[]

def ingresar(nomu, edadu):
    usuario = {
        'nombre': nomu,
        'edad': edadu
    }
    usuarios.append(usuario)

def mostrar():
    print("Usuarios")
    for i in range(len(usuarios)):
        print(usuarios[i])

    if len(usuarios)==0:
        print("La lista esta vacia, toma una buena coca cola")

nomu= input("Nombre de usuario (x para finalizar): ")
edadu= int(input("Edad: "))

while nomu!="x":
    ingresar(nomu, edadu)
    nomu=input("Nombre de usuario (x para finalizar): ")
    edadi=int(input("Edad: "))

mostrar()

#Axctividad 6
for i in range(len(usuarios)):
    mayorEdad(usuarios[i]['edad'])
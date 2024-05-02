#PARTE 2 - Actividad 1
class mascota:
    def __init__(self, especie, precio, vacunado, edad):
        self.especie = especie
        self.precio = precio
        self.vacunado = vacunado
        self.edad = edad
    pass
#PARTE 2 - Actividad 2
    def instancia(self):
        print(f'{self.especie}, {self.precio}, {self.vacunado}, {self.edad} años')

animal1 = mascota('Gato', 700, 'estoy vacunado', 2); animal1.instancia() 
animal2 = mascota('Perro', 600, 'estoy vacunado', 3); animal2.instancia() 
animal3 = mascota('Conejo', 800, 'estoy vacunado', 6); animal3.instancia() 
animal4 = mascota('Pato', 500, 'estoy vacunado', 4); animal4.instancia() 
animal5 = mascota('Camaleon', 1000, 'estoy vacunado', 5); animal5.instancia() 

#PARTE 2- Actividas 3 y 4
for i in range (5):
    lista_mascotas = [animal1.precio, animal2.precio, animal3.precio, animal4.precio, animal5.precio]
    lista_mascotas.sort()
    print(f"{i+1}.{lista_mascotas[i]}") 

#PARTE 2- Actividad 5
prom = (animal1.edad + animal2.edad + animal3.edad + animal4.edad + animal5.edad)/5
print("Promedio de edad de los animales: ", prom)

#PARTE 2 - Actividad 6
print("- - Animales vacunados - -")
for i in range (5):
    cant = [animal1.vacunado, animal2.vacunado, animal3.vacunado, animal4.vacunado, animal5.vacunado]
    print(f"{cant[i]}") 

    
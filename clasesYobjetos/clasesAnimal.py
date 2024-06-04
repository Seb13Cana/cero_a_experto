#Herencia en python
print('*** Herencia en python***')
#Clase padre
class Animal:
    def comer(self):
        print('Come muchas veces al dia')

    def dormir(self):
        print('Se acuesta a Mimir')

#Clase hija
class Perro(Animal):
    def ladrar(self):
        print('Woff Woff')

    def dormir(self):
        print('Se acuesta a Mimir como perrito')






print('Soy un animal')
animal_1 = Animal()
animal_1.comer()

animal_1.dormir()
#Accede a los metodos especificos y lo s de la clase padre
print('\nSoy un perro')
perro_1 = Perro()
perro_1.comer()
perro_1.ladrar()
perro_1.dormir()

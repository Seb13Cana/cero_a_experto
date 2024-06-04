#Se define la clase padre

class Animal:
    def comer(self):
        print(f'Como muchas cosas')

    def dormir(self):
        print(f'Duermo mucho tiempo')

#Clases hijas perro y gato
class Perro(Animal):
    def ladrar(self):
        print(f'Woff Woff')
    #Polimorfismo la clase dormir es difernete para perro pero tambien duerme
    def dormir(self):
        print(f'Duerme como perrito 15 horas')


class Gato(Animal):
    def ronronear(self):
        print(f'Rmm Rmm Rmm Rmm')
    #Polimorfismo  es diferente dormir como gato
    def dormir(self):
        print(f'Duerme como minino 18 horas')


print('Ejemplo de mpolimorfismo')

#Objegto clase padre
animal_1 = Animal()
animal_1.dormir()
print('\nClase hija Perro')
#Objeto clase hija/s
perro_1 = Perro()
perro_1.dormir()
print('\nClase hija Gato')
gato_1 = Gato()
gato_1.dormir()
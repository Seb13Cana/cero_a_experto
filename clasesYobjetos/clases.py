#Clase de contacto

class Contacto:
    #Atributos o caracteristicas
    def inicializar_contacto(self,nombre,apellido,celular,email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    #Metodos, acciones que realiza la clase, ejemplo mostrar contacto
    def mostrar_contacto(self):
        print(f'''
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Celular: {self.celular}
    Email: {self.email}
''')


#Codigo principal
print('*** Clases y objetos en Python ***')


contacto_1 = Contacto()
contacto_1.inicializar_contacto('David','Alarcon',3215467899,'david@email.com')
contacto_1.mostrar_contacto()
print(f'Dir de memoria: {id(contacto_1)}')
print(f'Dir de memoria: {hex(id(contacto_1))}')

contacto_2 = Contacto()
contacto_2.inicializar_contacto('Lucas','Gonzalez',3215678599,'lucas@emial.com')
contacto_2.mostrar_contacto()

lista = [15,'texto']

print(f'id lista: {id(lista)}')
for item in lista:
    print(f'Id objeto en memoria item: {id(item)}')
    print(f'Id hex objeto en memoria item: {hex(id(item))} ')


#Definir un constructor (__init__)

class Persona():

    def __init__(self,nombre,apellido):
        self._nombre   = nombre #Atributo protgid si se coloca _ al inicio
        self.__apellido = apellido #Atributo privado

    def mostrar_persona(self):
        print(f'''
    Nombre de la persona: {self._nombre}
    Apellido de la persona: {self.apellido}
''')

persona_1 = Persona('Diego','Jaramillo')

persona_1.mostrar_persona()
#Accedemos a los atributosde forma directa (Publicos)
persona_1.nombre = 'Ruth'
persona_1.apellido = 'Vasquez'
persona_1.mostrar_persona()
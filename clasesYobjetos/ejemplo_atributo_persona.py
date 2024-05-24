class Persona:
    #Variable o atributo de la clase
    contador_de_personas = 0

    #Constructor
    def __init__(self,nombre, apellido):
        #Incrementamos el contador y este se entrega como el id
        Persona.contador_de_personas += 1
        self.id = Persona.contador_de_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'id: {self.id}, nombre: {self.nombre}, apellido: {self.apellido}')




persona_1 = Persona('Raul', 'Vasquez')
persona_1.mostrar_persona()

persona_2 = Persona('David', 'Tellez')
persona_2.mostrar_persona()
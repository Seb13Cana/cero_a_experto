class Persona:
    def __init__(self, nombre,apellido):
       self.nombre = nombre
       self.apellido = apellido

    #Sobreescribir metodo __str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir memoria = {super.__str__(self)}

'''

persona_1 = Persona('Maria','Benitez')
print(persona_1)
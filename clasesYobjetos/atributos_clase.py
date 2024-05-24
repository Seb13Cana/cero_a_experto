class Persona:
    atributo_clase = 0

    def __init__(self):
        self.atributo_instancia = 0



print('*** Atributos de clase ***')

print(f'Atributo de clase {Persona.atributo_clase}')
#Modificar el atributo de clase
Persona.atributo_clase = 15
print(f'Atributo de clase {Persona.atributo_clase}')

#Crear el objeto
persona_1 = Persona()
persona_1.atributo_instancia = 25
print(f'El objeto Persona 1 Clase: {persona_1.atributo_clase}')
print(f'El objeto Persona 1 Instancia: {persona_1.atributo_instancia}')

#Crar segundo objeto
persona_2 = Persona()
persona_2.atributo_instancia = 36
print(f'El objeto Persona 1 Clase: {persona_2.atributo_clase}')
print(f'El objeto Persona 1 Instancia: {persona_2.atributo_instancia}')






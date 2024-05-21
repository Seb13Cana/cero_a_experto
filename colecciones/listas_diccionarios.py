print('*** Listas y diccionarios ***')

personas = [
    {'nombre': 'Luis', 'apellido': 'Flores', 'edad': 25},
    {'nombre': 'David','apellido':'Lopez', 'edad': 52}
]

print(personas)

print(personas[0])

#Acceder a un valor [llave]del primer dicc

print(personas[1].get('nombre'))

#rcorrer elementos de la lista

for contador, persona in enumerate(personas):
    print(f'persona {contador}: {persona.get("edad")}')
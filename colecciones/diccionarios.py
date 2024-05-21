print('*** Manejo de diccionarios ***')
#Almacena los diocmentos en forma llave : valor y no se pueden duplicarl los elementos
diccionario = {'nombre'  : 'David',
               'apellido': 'Lucas',
               'edad'    : 27}
print(diccionario)

#Acceder a los elementos

print(f'{diccionario["edad"]}')
print(f'{diccionario.get("nombre")}')

#El largo dse un diccionario

print(f'El largo del diccionario: {len(diccionario)}')

#Agregasr elemento
diccionario['telefono']= 22154

print(diccionario)

#Obtener lista de llaves

print(f'lista de llaves dic: {diccionario.keys()}')
print(f'Lista de valores del dicc: {diccionario.values()}')

#Recuperar llave y valor, items
print(f'Los elementos del dic son: {diccionario.items()}')

#Revisar siu la llave existe

llave__ = 'edad'

if llave__ in diccionario:
    print('Si')
else:
    print('no')

#actualizar o modificar elemento del dicc

diccionario['edad'] = 25

#Eliminar
diccionario.pop('telefono')
print(diccionario)

#Recorrer llavces

for llave_ in diccionario.keys():
    print(llave_)

#Recorrer vlores

for valor in diccionario.values():
    print(valor)

#Recorrer elemento

for llave, valor in diccionario.items():
    print(f'Llave: {llave}, valor: {valor}')
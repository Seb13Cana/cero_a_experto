print('*** Argumewntos por nombre ***')

def crear_persona(nombre, apellido ='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

#Llamamos a la función

crear_persona('Ricardo', 'Cruz', 54)
crear_persona(nombre='David',edad=25)
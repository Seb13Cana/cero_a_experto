import random

#Ingresar datos del habitante

#Nombre, apellido, año de nacimiento

nombre          = input('Cual es tu nombre?: ')

apellido        = input('Cual es tu apellido?: ')

anio_nacimiento = input('Cual es tu Año de nacimiento? (YYYY): ')

#recuperandfo las cadenas de nombre apellido y año

sigla_nombre = nombre[0:2].upper()
sigla_apellido = apellido[0:2].upper()
sigla_anio = anio_nacimiento[2:4]

#genera ultimos 4 numeros del indice

str_sigla_random = str(random.randint(0,9999))

#ID unico generado
id_generado = sigla_nombre+sigla_apellido+sigla_anio+str_sigla_random
print(f'''
Hola {nombre}, habitante de ciudad gotica!
    Tu nuevo numero de identificación (ID) generado por el sistema es:
    {id_generado}
    Felicidades!

''')
print('*** Regresar tupla de valore desde una funcion ***')


#Definir la función
def persona_mayuscula(nombre, apellido, edad=0):
    print('Esta funcion regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad


#Programa principal
#Se deben desempacar todos los valores que retorna l atupla de la función, si son 3, se deben asignar a 3 variables 
nombre, apellido, edad = persona_mayuscula('David','jimenes')

print(f' el nombre {nombre}, apellido {apellido}, edad {edad}')
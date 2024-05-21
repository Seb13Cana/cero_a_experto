print('***Listas en python ***')
nombres = ['Lucas', 'Pedro', 'Thomas']

print(nombres)

for nombre in nombres:
    print(f'Los nombres de los discipulos son: {nombre}')

#Las listas pueden ser heterogeneas

lista_heterogenea = [250, True, 'Marta', 256.35]

print('Datos lista heterogenea')
for item in lista_heterogenea:
    print(item)

#Recuperar elemento de la lista
numeros = [1,2,3,4,5,6]
print(numeros[1])

#Modificar elementos
#print(numeros[2])
#numeros[2] = 8
#print(numeros[2])

#Buscar elementos
numero_a_buscar = 5

if numero_a_buscar in numeros:
    print(f'si se encuentra el numero {numero_a_buscar} en la lista')
else:
    print(f'no se encuentra el numero: {numero_a_buscar} en la lista')

#Recuperar indices
indice = numeros.index(numero_a_buscar)

print(f'El indice de {numero_a_buscar} en la lista numeros es: {indice}')

#Recuperar tramos de la lista
numeros = [1,5,2,3,6,22,18,0,11,4]
numeros_recuperados = numeros[0:4]
print(numeros_recuperados)
#Sin indicaf el indice inicial
numeros_recuperados= numeros[:3]
print(numeros_recuperados)
#sin indicar el indice final
numeros_recuperados = numeros[7:]
print(numeros_recuperados)


#metodos
# hallar el largo de una lista len
largo_de_una_lista = len(numeros)
print(largo_de_una_lista)
# Agregar item a la lista
numeros.append(54)
print(numeros)
#insertar elementos en el indice deseado
numeros.insert(4,66)
print(numeros)
#eliminar por indice
del numeros[3] #Elimina elemento por el indice

#Eliminar losta, lo qie se hace es vaciar la lista

numeros[:] = []

del numeros #Elimina la variable de la lista
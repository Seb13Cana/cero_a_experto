print('*** Manejo de Tuplas ***')

nombres = ('Karla', 'Juan', 'Pedro')

print(nombres)

tupla_heterogenea = 100,500,'Ursula' #Los parentesis son opcionales
print(type(tupla_heterogenea))

#Recorrer elementos de una tupla

for nombre in nombres:
    print(nombre, end=' - ')

numeros = 100,200,300,400,500

print(f'Para el indice 0 el valor de la tupal es: {numeros[0]}')
print(f'Para el indice -1 el valor de la tupal es: {numeros[-1]}')

#No se pueden modifica los elementos en las tuplas
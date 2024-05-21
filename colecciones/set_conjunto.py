print('** Manejo de Set o conjunto en python ***')

#Un set es un conjunto de datos no ordenados, no soporta acciones que incuyan indices o similares

conjunto = {1,2,5,'Karla', True, 8.3, 'Karla', 'David'}

print(conjunto)

for item in conjunto:
    print(item)

numero_a_buscar = 55

if numero_a_buscar in conjunto:
    print(f'el numero a buscar {numero_a_buscar} si se encuentra en el conjunto')
else:
    print(f'el numero a buscar {numero_a_buscar} no se encuentra en el conjunto')

conjunto.add(450)

print(conjunto)
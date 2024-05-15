# Formato de cadenas Python
var_hola  = 'Hola'
var_mundo = 'Mundo'

#Imprimir valores

print(var_hola,var_mundo)

# Concatenar cadenas

var_hola_mundo = var_hola +' '+ var_mundo

print(var_hola_mundo)

# Interpolar caenas

var_hola_mundo =  f'Mi caden {var_hola} {var_mundo}'

print(var_hola_mundo)

#Int4rpolar cadenas multiple lineas f''' '''

print(f'''Hola este es un texto multilineas
Donde se estan ingresando algunas variables como : {var_hola} y {var_mundo}''')
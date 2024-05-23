from modulo import saludar
print('*** Manejo de funciones ***')



#2. Llamamos a la  fiunción
argumento = input('Ingrersa el mensaje a enviar: ')
valor_devuelto = saludar(argumento)
print(f'Valore devuelto {valor_devuelto}')

saludar(argumento)
saludar('Saludos')
saludar('Adios')
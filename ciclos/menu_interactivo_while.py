#Menu interactivo con ciclo while

print('*** Sistema e administración de cuentas ***')

salir = False

while not salir:

    print(f'''
    1. Crear Menu
    2. Eliminar cuenta
    3. Salir.
    ''')
    opcion = int(input(f'Por favor escoja una opcion'))
    if opcion ==1:
        print('Creando cuenta...')
    elif opcion ==2:
        print('Eliminando cuenta')
    elif opcion ==3:
        print('Saliendo del sistema')
        salir = True
    else:
        print('Escoja una opcion valida')

print('saliendso del sistema, hasta pronto.')
#Reto calculadoa con funciones

def mostrar_menu():
    print(f'''
    1. Suma
    2.Resta
    3.Division
    4.Multiplicacion
    5.Salir
''')
    opcion = int(input('Escoje una opción: '))
    return opcion

def pedir_valores():
    valor_1 = float(input('Ingresa el valor 1: '))
    valor_2 = float(input(('Ingresa el valor 2: ')))
    return valor_1, valor_2

def ejecutar_opereciones(opcion,salir):
    if opcion == 1:
        valor_1, valor_2 = pedir_valores()
        print(f'el resultado de la suma es: {valor_1 + valor_2}')
    elif opcion == 2:
        valor_1, valor_2 = pedir_valores()
        print(f'el resultado de la resta es: {valor_1 - valor_2}')

    elif opcion == 3:
        valor_1 , valor_2 = pedir_valores()
        print(f'el resultado de la division es: {valor_1 / valor_2}')
    elif opcion == 4:
        valor_1 , valor_2 = pedir_valores()
        print(f'el resultado de la multiplicación  es: {valor_1 * valor_2}')
    elif opcion == 5:
        salir = True
        print('Gracias, regresa pronto')
    else:
        print('Ingresa una opción valida.')

    return  salir
#Codigo principal
salir = False

while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_opereciones(opcion,salir)


snacks = [
    {'id': 0, 'nombre': 'Galletas', 'precio': 250.00},
    {'id': 1, 'nombre': 'Papas', 'precio': 315.00},
    {'id': 2, 'nombre': 'Jugo', 'precio': 400.00}
]

#Definir lista se productos qque se compraran
productos = []

print('*** Maquina de snacks ***')
print('Snacks disponibles: ')

for snack in snacks:
    print(f'\tId: {snack["id"]} -> {snack["nombre"]}: ${snack["precio"]}')


def maquina_de_snacks(snacks,productos = []):
    salir = False
    while not  salir:
        print(f'''
        1. Comprar snack
        2. Mostrar factura
        3. salir
''')
        opcion = int(input('Seleccione un opción: '))
        if opcion==1:
            comprar_producto(snacks,productos)
        elif opcion ==2:
            mostrar_ticket(productos)
        elif opcion ==3:
            print('Regresa pronto')
            salir= True


def comprar_producto(snacks,productos):
    id_snack =  int(input(f'Ingresa el ID del snack: '))
    productos.append(snacks[id_snack])
    print(f'Snack: {snacks[id_snack]} agregado')

def mostrar_ticket(productos):
    ticket = f'\t *** Ticket de venta'
    total_ticket = 0
    for producto in productos:
        ticket += f"\n\t- {producto['nombre']} - ${producto['precio']}"
        total_ticket += producto['precio']

    ticket += f'\n\t TOTAL: ${total_ticket}'
    print(ticket)


#"Llamamos la funcipn de maquina de snacks"

maquina_de_snacks(snacks,productos)
from proyectos.snack import Snack
from proyectos.snacks import Snacks

snacks = Snacks()

print(snacks)

#Definir lista se productos qque se compraran
productos = []

print('*** Maquina de snacks ***')
print('Snacks disponibles: ')

#for snack in snacks:
#    print(f'\tId: {snack["id"]} -> {snack["nombre"]}: ${snack["precio"]}')


def maquina_de_snacks(snacks,productos ):
    salir = False
    while not  salir:
        print(f'''
        1. Comprar snack
        2. Mostrar factura
        3. Agregar Snack
        4. Salir
''')
        opcion = int(input('Seleccione un opción: '))
        if opcion==1:
            comprar_producto(snacks,productos)
        elif opcion ==2:
            mostrar_ticket(productos)
        elif opcion == 3 :
            agregar_snack(snacks)
        elif opcion ==4:
            print('Regresa pronto')
            salir= True


def comprar_producto(snacks,productos):
    id_snack =  int(input(f'Ingresa el ID del snack: '))
    #productos.append(snacks[id_snack])
    #print(f'Snack: {snacks[id_snack]} agregado')
    #Recorre  la lista de snackas para saber si existe en la lista
    snack_encontrado = None
    for snack in snacks.lista_snacks:
        if id_snack == snack.id:
            snack_encontrado = snack
            break
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'el snack {snack_encontrado}, si se encuentra en la lista')
    else:
        print(f'El snack id: {id_snack}, no se encuentra en la lista')


def mostrar_ticket(productos):
    ticket = f'\t *** Ticket de venta'
    total_ticket = 0
    for producto in productos:
        ticket += f"\n\t- {producto.nombre} - ${producto.precio}"
        total_ticket += producto.precio

    ticket += f'\n\t TOTAL: ${total_ticket}'
    print(ticket)

def agregar_snack(snacks):
    nombre = input('Ingresa el nombre del snack: ')
    precio = int(input('Ingresa el precio del snack: '))
    nuevo_snack = Snack(nombre,precio)
    snacks.agregar_snack(nuevo_snack)
    print(f'El Snack {nuevo_snack} se ha agregadio correctamente')
    print(snacks)

#"Llamamos la funcipn de maquina de snacks"

maquina_de_snacks(snacks,productos)
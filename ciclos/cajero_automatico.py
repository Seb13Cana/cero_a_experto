#Cajero automatico ciudad gotica

print('*** Cajero automatico (ATM) de ciudad Gotica ***')

salir = False
saldo_inicial = 1000.00

while not salir:
    print(f'''
Operaciones que puedes realizar:
1. Consultar Saldo
2. Retirar
3. Depositar
4. Salir
''')

    opcion = int(input(f'Por favor ingresa una opción: '))


    if opcion ==1:
        print(f'Tu saldo actual es: ${saldo_inicial:.2f}')
    elif opcion ==2:
        monto_a_retirar = float(input('Ingresa el valor a retirar: '))
        if monto_a_retirar <= saldo_inicial and  monto_a_retirar > 0 :
            saldo_inicial -= monto_a_retirar
            print(f'Nuevo saldo actiual ${saldo_inicial:.2f}')
        else:
            print(f'No es posible realizar la acción, tu saldo actual es {saldo_inicial:.2f}')
    elif opcion ==3:
        monto_a_depositar = float(input('Ingresa el valor a depositar: '))
        saldo_inicial += monto_a_depositar
        print(f'Nuevo saldo actiual ${saldo_inicial:.2f}')
    elif opcion ==4:
        print('Saliendo')
        salir = True
    else:
        print(f'Opcion invalida, seleciona otra opcion')
#Ingreso de datos
print('*** Bienvenidoal sistema de generación de email de ciudad gotica ***')
nombre   = input('Ingresa tu nombre por favor: ').lower()
apellido = input('Ingresa tu apellido por favor: ').lower()

email_generado = f'{nombre}.{apellido}@ciudadgotica.com'

print(f'''Tu nuevo email generado por el sistema es:
    {email_generado}
    *** Felicidades ***''')


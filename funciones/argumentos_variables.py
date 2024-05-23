print('*** Argumentos Variables ***')

#Definimos la funcion
#*args -> arguments -> tupla
#-> **kwargs -> keyword arguments -> diccionario
def superheroe_poderes(nombre, *args, **kwargs):
    print(f'Super heroe: {nombre} - {args}- mas info: {kwargs}')
    for poder in args:
        print(poder)

#Llamaos la funcion

superheroe_poderes('Spiderman', 'Spider sense', 'Lanza telaraña',
                   edad=17,empresa='Marvel')
superheroe_poderes('Iron Man', 'filantropo', 'playboy', 'millonario')

#Es opcional envir los argumonetosde variales
superheroe_poderes('la mama')
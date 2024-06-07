class Snack:
    contador_snacks = 0

    def __init__(self,nombre, precio):
        Snack.contador_snacks +=1
        self.id = Snack.contador_snacks
        self.nombre = nombre
        self.precio = precio


    def __str__(self):
        return f'''Snack Id: {self.id}
        Nombre: {self.nombre}, Precio: ${self.precio}'''

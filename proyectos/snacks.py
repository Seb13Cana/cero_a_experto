from proyectos.snack import Snack


class Snacks:
    lista_snacks = [
        Snack('Papas', 75),
        Snack('Oreo', 85),
        Snack('Red Bull', 100)
    ]

    def agregar_snack(self,snack):
        Snacks.lista_snacks.append(snack)

    def __str__(self):
        snacks_str = ''
        for snack in Snacks.lista_snacks:
            snacks_str += '\n' + snack.__str__()

        return f'''*** Snacks en el inventario***
                {snacks_str}
                '''
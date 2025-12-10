from padre import Botella
class Botella_plastica(Botella):
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_color, dato_tamano): #init hijo
        super().__init__(dato_material, dato_capacidad, dato_forma) #init padre
        self.color=dato_color
        self.tamano=dato_tamano
    def imprimir_datos(self):
        dato_mensaje=super().imprimir_datos()
        mensaje=dato_mensaje + f"El color de la botella es {self.color} y su tamaño es {self.tamano}"

        print(mensaje)

from carro import Carro

class Van(Carro):
    def __init__(self, modelo, color, motor, numeroPuertas, capaPasa, tipoComb):
        super().__init__(modelo, color, motor, numeroPuertas, capaPasa, tipoComb)
    
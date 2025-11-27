class Carro:
    def __init__(self, modelo, color, motor, numeroPuertas, capaPasa, tipoComb):
        self.modelo=modelo
        self.color=color
        self.motor=motor
        self.numeroPuertas=numeroPuertas
        self.capaPasa=capaPasa
        self.tipoComb=tipoComb
        
    def arranque(self, tipoArranque):
        mensaje=f"El tipo de arranque es {tipoArranque}. "
        return mensaje
    
    def acefren(self, tAcel, tFren):
        mensaje=f"Acelera de 0 a 100 en {tAcel} segundos y frena de 100 a 0 en {tFren} metros. "
        return mensaje
    
    def luces(self, tLuz):
        mensaje=f"las luces son {tLuz}. "
        return mensaje
    
    def ventanas(self, tVen):
        mensaje=f"Las ventanas son {tVen}. "
        return mensaje
    
    def printData(self):
        mensaje=f"El vehiculo es un {self.modelo} {self.numeroPuertas} puertas color {self.color}, con un motor {self.motor} a {self.tipoComb}, con capacidad para {self.capaPasa} personas. "
        return mensaje



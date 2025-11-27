from carro import Carro

myCar=Carro("Mazda", "Rojo", "V8", "4", "5", "gasolina")
arranque = myCar.arranque("push")
acefren = myCar.acefren("10", "32")
luces = myCar.luces("Halogenas")
ventanas = myCar.ventanas("Automaticas")
combo=myCar.printData() + arranque + acefren + luces + ventanas
print(combo)
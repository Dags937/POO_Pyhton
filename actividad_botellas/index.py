from padre import Botella
from hijo1 import Botella_plastica
from hijo2 import Botella_vidrio
from base_datos import Base_datos

#codigo principal
obj_base_datos=Base_datos()
#hacer el objeto
material=input("Seleccione el material de la botella:")
capacidad=input("La capacidad de la botella es:")
forma=input("La forma de la botella es :")
obj_botella=Botella(material, capacidad, forma)
obj_botella.material #atributo
dato_atributo = obj_botella.get_material()
dato_liquido = obj_botella.contener_liquido("Nestea")
print(dato_liquido)

obj_botella_plastica=Botella_plastica("Plastico", "3 Litros", "Ovalada", "Rojo Translucido", "Grande")
imprimir_plastico=obj_botella_plastica.imprimir_datos()
print(imprimir_plastico)

obj_botella_vidrio=Botella_vidrio("Vidrio", "2 litros", "circular", "templado", "grande")
imprimir_vidrio=obj_botella_vidrio.imprimir_datos()

print(imprimir_vidrio)

base_datos.guardar_objeto(obj_botella)



class Base_datos:
  def __init__(self):
    self.lista_botellas=[]
    self.lista_plastico=[]

  def guardar_obj(self, nuevo_obj):
    self.lista_botellas.append(nuevo_obj)

  def agregar_varios_obj(self, lista_nueva):
    self.lista_botellas.extend(lista_nueva)

  def imprimir_info(self):
    for obj in self.lista_botella:
      print(obj)

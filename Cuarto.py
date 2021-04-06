
from dibujos import*
from api import*
from Objeto import*

class Cuarto:
    def __init__(self, name, drawing, obj_izq, obj_centro, obj_derecha):
        self.name = name
        self.drawing = drawing
        self.obj_izq= obj_izq
        self.obj_centro= obj_centro
        self.obj_derecha= obj_derecha

    def show_room(self):
        print(self.drawing)

biblioteca = Cuarto('biblioteca', biblioteca_drawing, mueble_sentarse ,mueble_libros, mueble_gabetas)

plaza_rectorado = Cuarto('plaza_rectorado', plaza_rectorado_drawing, banco1, saman, banco2 )

laboratorio = Cuarto('laboratorio', laboratorio_drawing, compu1, pizarra, compu2)

pasillo_laboratorios = Cuarto('pasillo_laboratorios', pasillo_laboratorios_drawing, None, puerta_pasilo, None)

cuarto_servidores = Cuarto('cuarto_servidores', cuarto_servidores_drawing, rack, puerta_servidores, papelera)


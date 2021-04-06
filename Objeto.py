from api import*

class Objeto:
    def __init__(self, dict):
        self.name = dict['name']
        self.position = dict['position']
        self.game = dict['game']


# objetos laboratorio

pizarra = Objeto(pizarra_dict)
compu2 = Objeto(compu2_dict)
compu1 =Objeto(compu1_dict)

#objetos biblioteca

mueble_libros = Objeto(mueble_libros_dict)
mueble_gabetas = Objeto(mueble_gabetas_dict)
mueble_sentarse = Objeto(mueble_sentarse_dict)

#objetos plaza rectorado
saman = Objeto(saman_dict) 
banco1 = Objeto(banco1_dict)
banco2 = Objeto(banco2_dict)

#objetos pasillo laboratorio
puerta_pasilo = Objeto(puerta_pasillo_dict)

#objetos cuarto servidores
puerta_servidores = Objeto(puerta_servidores_dict)
rack = Objeto(rack_dict)
papelera = Objeto(papelera_dict)


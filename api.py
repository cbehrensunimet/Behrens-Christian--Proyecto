import requests

def objetos_api():
    '''
    Devuelve los datos de la API en forma de diccionario
    '''
    url = 'https://api-escapamet.vercel.app/'
    response = requests.request('Get', url)

    return response.json()

api = objetos_api()

#diccionarios para cada cuarto
laboratorio_dict = api[0]
biblioteca_dict = api[1]
plaza_rectorado_dict = api[2]
pasillo_laboratorios_dict = api[3]
cuarto_servidores_dict = api[4]

#diccionarios de los objetos del laboratorio
pizarra_dict = laboratorio_dict['objects'][0]
compu1_dict = laboratorio_dict['objects'][1]
compu2_dict = laboratorio_dict['objects'][2]

#diccionarios de los objetos de la biiblioteca
mueble_libros_dict =  biblioteca_dict['objects'][0]
mueble_sentarse_dict = biblioteca_dict['objects'][1]
mueble_gabetas_dict = biblioteca_dict['objects'][2]

#diccionarios de los objetos de la plaza rectorado
saman_dict = plaza_rectorado_dict['objects'][0]
banco1_dict = plaza_rectorado_dict['objects'][1]
banco2_dict = plaza_rectorado_dict['objects'][2]

#diccionarios de los objetos del pasillo de laboratorios
puerta_pasillo_dict = pasillo_laboratorios_dict['objects'][0]

#diccionarios de los objetos del cuarto servidores
puerta_servidores_dict = cuarto_servidores_dict['objects'][0]
rack_dict = cuarto_servidores_dict['objects'][1]
papelera_dict =  cuarto_servidores_dict['objects'][2]



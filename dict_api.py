import requests

def dict_api():
    '''
    Devuelve los datos de la API en forma de diccionario
    '''
    url = "https://api-escapamet.vercel.app/"
    response = requests.request('Get', url)

    return response.json()

api = dict_api()




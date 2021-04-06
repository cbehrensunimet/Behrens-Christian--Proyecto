from Usuario import *
import os
import pickle

def cargar_datos_txt(archivo, datos):
    '''
    Carga datos a un archivo externo
    Recibe: Nombre del archivo y datos a cargar
    Devuelve: Void
    '''
    escritura_binaria = open(archivo, 'wb')
    datos = pickle.dump(datos, escritura_binaria)
    escritura_binaria.close()

def recibir_datos_txt(archivo, datos):
    '''
    Extrae datos de un archivo externo
    Recibe: Nombre del archivo y lista donde recibimos los datos
    Devuelve: lista con los datos extraídos del archivo externo
    '''
    lectura_binaria = open(archivo, 'rb')
    if os.stat(archivo).st_size != 0:

        datos = pickle.load(lectura_binaria)
    lectura_binaria.close()
    return datos

def check_password(password):
    '''
    Revisa las condiciones que deben darse para que la contraseña sea válida.
    Esta no puede tener menos de 8 caracteres, no puede tener espacios y debe tener al menos una mayúscula, una minúscula, un carácter no alfanumérico y un número
    Recibe: Contraseña ingresada por el usuario
    Devuelve: True si la contraseña es válida y False si no lo es
    '''
    lenght = len(password)
    espacio = False
    num = False
    mayus = False
    minus = False
    alfanum = False 
    for letter in password:
        if not letter.isspace():
            espacio = True
        if letter.isnumeric():
            num = True
        if letter.isupper():
            mayus = True
        if letter.islower():
            minus = True 
        if not letter.isalnum():
            alfanum = True
        
    if espacio and num and mayus and minus and alfanum and lenght > 7:
        return True
    else:
        return False

def check_username(username,users):
    '''
    Revisa que el nombre de usuario no exista en la base de datos
    Recibe: nombre de usuario que se desea registrar y lista de usuarios registrados
    Devuelve: True si está disponible; False si ya existe
    '''

    users = recibir_datos_txt('lista_users.txt', users )
    for u in users:
        if u.username == username:
            return False

    return True

def sign_up(users):
    """
    Registra usuarios nuevos en la base de datos
    Recibe: Lista de usuarios
    Devuelve: Lista de usuarios con nuevo usuario registrado
    """
    os.system('clear')
    username = input('Username: ')
    for i in username:
        if i == ' ':
            print('El sistema ha reemplazado ' ' por _')

    username = username.replace(' ', '_')
    while not check_username(username, users):
        print('Este nombre de usuario no está disponible')
        username = input('Nombre de usuario: ')

    password = input('Contraseña: ')
    while not check_password(password):
        print('La contraseña debe tener como mínimo 8 caracteres, no tener espacios y tener por lo menos una mayúscula, una minúscula, un número y un caracter especial.') 
        password = input('Contraseña: ')

    age = input('Ingrese su edad: ')
    while int(age) < 0 or (not age.isnumeric()):
        print('Ingreso inválido')
        age = input('Ingrese su edad: ')

    avatar =str(input('Ingrese el número del avatar que desea utilizar\n1- Scharifker\n2- Eugenio Mendoza\n3- Pelusa\n4- Gandhi\n>>'))

    while (avatar != "1") and (avatar != "2") and (avatar != "3") and (avatar != "4"):
        print('Ingreso inválido ')
        avatar = str(input('Ingrese el número del avatar que desea utilizar\n1- Scharifker\n2- Eugenio Mendoza\n3- Pelusa\n4- Gandhi\n>>'))
    if avatar == '1':
        avatar = 'scharifker'
    if avatar == '2':
        avatar = 'eugenio mendoza'
    if avatar == '3':
        avatar = 'pelusa'
    if avatar == '4':
        avatar = 'gandhi'

    new_user = Usuario(username, password, age, avatar)
    users.append(new_user)
    os.system('clear')
    print('Registro exitoso!')
    new_user.show_attributes()
    print('')

    return users
    
def sign_in(users):
    '''
    Verifica si un usuario está en la base de datos 
    Recibe: lista usuarios
    Devuelve: Usuario activo si el usuario está en la base de datos y la contraseña coincide y None si el usuario no está en la base de datos
    '''
    os.system('clear')
    while True:
        users = recibir_datos_txt('lista_users.txt', users )

        active_user = input('Ingrese su username: ')
        for user in users:
            if active_user == user.username:

                password = input('Ingrese su contraseña: ')
                while password != str(user.get_password()):
                    print('Contraseña incorrecta')
                    print('Ingrese [0] si olvidó su contraseña y desea salir')
                    password = input('Ingrese su contraseña: ')
                    if password == '0':
                        os.system('clear')
                        return None
                os.system('clear')
                print('Inicio de sesión exitoso!')
                user.show_attributes()
                print('')
                active_user = user
                return active_user
        os.system('clear')
        print('Usuario no registrado\n')
        return None

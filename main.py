from functions_user import *
from Usuario import *
from functions_player import*
from Jugador import*
from functions_play import*
import time
from Cuarto import*
from functions_records import*
from art import*
import os 
from fecha import*

def main():
    users = [] #lista donde se van a almacenar los usuarios
    users = recibir_datos_txt('lista_users.txt', users )
    records = [] #lista donde se van a almacenar los records
    records = recibir_datos_txt('records.txt', records)
    matches = [] #lista donde se van a almacenar los datos de cada partida
    matches = recibir_datos_txt('matches.txt', matches)
    active_user = False
    
    
    os.system('clear')

    while True:
        signed_user = None
        new_user = None
        
        opcion = input('Bienvenido! Seleccione una de las siguienes opciones:\n1- Nueva Partida\n2- Instrucciones del juego\n3- Ver Récords\n4- Salir\n>>')
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
           opcion = input('Ingreso inválido\nDebe Ingresar el número de la opción que desea realizar\n>> ')

        if opcion == '1':
            os.system('clear')
            print('Para jugar debe tener una cuenta activada; indique si desea registrarse o iniciar sesión\n')
            sel_user = input('1- Registrarse\n2- Iniciar sesión\n3- Volver\n>>')
            while sel_user != '1' and sel_user != '2' and sel_user != '3':
                print('Ingreso inválido')
                sel_user = input('1- Registrarse\n2- Iniciar sesión\n3- Volver\n>>')
            if sel_user == "1":
                users = sign_up(users)
                cargar_datos_txt('lista_users.txt', users)
                new_user = users[-1]
                active_user = True

            elif sel_user == "2":
                signed_user = sign_in(users)
                nwe_user = None
                if signed_user != None:
                    active_user = True

            elif sel_user == "3":
                os.system('clear')

            while active_user: #verifica que el usuario haya iniciado sesión o se haya registrado
                difficulty = set_difficulty()
                playtime = set_time(difficulty)
                lives = set_lives(difficulty)
                hints = set_hints(difficulty)
                starting_room = biblioteca.name

                if new_user != None:
                    player = Jugador(new_user.username, new_user.get_password(), new_user.age, new_user.avatar, lives, hints, difficulty, starting_room)
                elif signed_user != None:
                    player = Jugador(signed_user.username, signed_user.get_password(), signed_user.age, signed_user.avatar, lives, hints, difficulty, starting_room)
                #primera narrativa
                os.system('clear')
                print(f'Hoy {day} de {month} de {year}, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {playtime} minutos, antes de que el servidor se caiga y no se pueda hacer más nada.')
                op = input('\n ¿Aceptas el reto? [S] Si\n>>').lower()
                while op !='s':
                    op = input('\n Tómate tu tiempo... Presiona [S] cuando estés listo\n>>').lower()
                os.system('clear')


                tprint('BIENVENIDO')
                #segunda narrativa
                
                print(f'Bienvenido {player.username}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.\n')
                random_password = random.randint(1000,9999)
                t = input('Presione cualquier tecla para empezar la partida...')
                os.system('clear')
                #inicia el juego
                #inicia el tiempo
                time_limit = playtime * 60
                start_time = time.time() #inicia el tiempo
                end_time = start_time + time_limit

                while True:

                    while active_user != False:
                        
                        time_past = (time.time() - start_time)
                        remaining_time = time_limit - time_past
                        final_time = round(time_past/60, 2)
                        print(f'\nTiempo Restante: {round(remaining_time/60)} minutos')

                        play(player, active_user, random_password, biblioteca, plaza_rectorado, pasillo_laboratorios, cuarto_servidores, laboratorio)
                        
                        if time_past > time_limit:
                            active_user = False
                            player.set_time(playtime)
                            print('Se ha agotado el tiempo')
                            tprint('GAME OVER')

                        elif player.lives <= 0:
                            active_user = False
                            player.set_time(final_time)
                            print('Te quedaste sin vidas')
                            tprint('GAME OVER')

                        elif player.winner == True:
                            player.set_time(final_time)
                            tprint("WINNER",font="block",chr_ignore=True)
                            #narrativa final
                            print(f'¡Felicidades! Has logrado evitar una catástrofe en la Unimet, y no solo eso, sino que ahora el casino está abierto para todo público!. ¡Los estudiantes mayores de 18 años ahora pueden apostar sus puntos obtenidos por créditos en el casino! (Ya que apostar dinero no sería éticamente correcto) \nCompletaste una esta misión de nivel {player.difficulty} en {player.finish_time} minutos. ¡Vuelve a jugar para romper esos récords!')
                            active_user = False
                    
                    if active_user == False: #se acaba la partida

                        matches = new_match(matches, player)
                        cargar_datos_txt('matches.txt', matches)
                        print('Partida cargada')

                        if new_user != None:
                            records = new_record(records, player)
                            cargar_datos_txt('records.txt', records)
        
                        else:
                            records = update_records(records, player)
                            cargar_datos_txt('records.txt', records)

                        input('Presione cualquier tecla para volver al menú principal')
                        os.system('clear')
                        break
                    
        if opcion == '2':
            os.system('clear')
            tprint('INSTRUCCIONES')
            f = open('Instrucciones.txt','r')
            instrucciones = f.read()
            f.close()
            print(instrucciones)
            t = input('Presione cualquier tecla para volver al menú principal')
            os.system('clear')

        if opcion == '3':
            os.system('clear')
            sel = input('1-Top 5 partidas\n2-Cuartos más visitados por jugador\n3-Usuarios con más partidas\n>>')
            while sel != '1' and sel != '2' and sel != '3':
                print('Ingreso inválido')
                sel = input('1-Top 5 partidas\n2-Cuartos más visitados por jugador\n3-Usuarios con más partidas\n>>')
            if sel == '1':
                os.system('clear')
                top_matches(matches)
                t = input('Presione cualquier tecla para volver al menú principal')
                os.system('clear')
            elif sel == '2':
                os.system('clear')
                cuartos_mas_visitados(records)
                t = input('Presione cualquier tecla para volver al menú principal')
                os.system('clear')
            elif sel == '3':
                os.system('clear')
                partidas_usuarios(records)
                t = input('Presione cualquier tecla para volver al menú principal')
                os.system('clear')
    
        if opcion == '4':
            os.system('clear')
            print('Hasta luego!')
            break

main()
from Jugador import *
from Cuarto import*
from Adivinanza import*
from Ahorcado import*
from Blackjack import*
from Criptograma import*
from Logica_booleana import*
from Logica_emojis import*
from Numero_entre import*
from Palabra_desordenada import*
from Pregunta_matematica import*
from Quiziz import*
from Sopa_de_letras import*
from Preguntas_python import*
from Memoria import*
import os

def play(player, user, random_password,biblioteca, plaza_rectorado, pasillo_laboratorios, cuarto_servidores, laboratorio):
    '''
    Funcion del juego
    '''
    extra_life1 = 1 #vida extra saman
    extra_life2 = 1 #vida extra pizarra
    door_open = False

    juego_puerta = Logica_Booleana(pasillo_laboratorios.obj_centro.game)
    juego_banco1 = Quiziz(plaza_rectorado.obj_izq.game)
    juego_saman = Logica_emojis(plaza_rectorado.obj_centro.game)
    juego_banco2 = Memoria(plaza_rectorado.obj_derecha.game)
    juego_compu1 = Pregunta_python(laboratorio.obj_izq.game)
    juego_pizarra = Sopa_de_letras(laboratorio.obj_centro.game)
    juego_compu2 = Adivinanza(laboratorio.obj_derecha.game, random_password)
    juego_rack = Palabra_desordenada(cuarto_servidores.obj_izq.game, random_password)
    juego_final = BlackJack(cuarto_servidores.obj_centro.game)
    juego_papelera= Numero_entre(cuarto_servidores.obj_derecha.game)
    juego_mueble = Pregunta_matematica(biblioteca.obj_izq.game)
    juego_libros = Ahorcado(biblioteca.obj_centro.game)
    juego_gaveta = Criptograma(biblioteca.obj_derecha.game)

    if player.room == biblioteca.name and (player.lives > 0) and (player.winner == False):
        player.in_room(biblioteca.name)

        print(biblioteca_drawing)
        player.show_attributes()
        print('\n')
        sel = input('>>').lower()
        if sel == 'a':
            os.system('clear')
            player.set_room(plaza_rectorado.name)
        elif sel == 'd':
            os.system('clear')
            player.set_room(pasillo_laboratorios.name)
        elif sel == '1':
            os.system('clear')
            juego_mueble.game(player)

        elif sel == '2':
            os.system('clear')
            juego_libros.game(player)

        elif sel == '3':
            os.system('clear')
            juego_gaveta.game(player)
        else:
            os.system('clear')
            

    elif player.room == plaza_rectorado.name and (player.lives > 0) and (player.winner == False):
        player.in_room(plaza_rectorado.name)
  
        plaza_rectorado.show_room()
        player.show_attributes()
        print('\n')
        sel = input('>>').lower()
        if sel == 'd':
            os.system('clear')
            player.set_room(biblioteca.name)
        elif sel == '1':
            os.system('clear')
            juego_banco1.game(player)
  

        elif sel == '2':
            os.system('clear')
            juego_saman.game( player) 

        elif sel == '3':
            os.system('clear')
            juego_banco2.game(player)

        elif sel == 'vida': #easter egg vida
            os.system('clear')
            if 'hoja del saman' not in player.inventory:
                player.add_lives(extra_life1)
                player.add_to_inventory('hoja del saman')
            else:
                print('Ya reclamaste esta vida extra ')
        else:
            os.system('clear')
                
    elif player.room == pasillo_laboratorios.name and (player.lives > 0) and (player.winner == False):
        player.in_room(pasillo_laboratorios.name)
    
        pasillo_laboratorios.show_room()
        if juego_puerta.award in player.inventory:
            print('¡LA PUERTA ESTÁ ABIERTA!\n')
        player.show_attributes()
        print('\n')
        sel = input('>>').lower()
        if sel == 'a':
            player.set_room(biblioteca.name)
            os.system('clear')
        elif sel == '2':
            if juego_puerta.award not in player.inventory :
                os.system('clear')
                juego_puerta.game(player)

            else:
                os.system('clear')
                player.set_room(laboratorio.name)
        else:
            os.system('clear')

    elif player.room == laboratorio.name and (player.lives > 0) and (player.winner == False):
        player.in_room(laboratorio.name)

        laboratorio.show_room()
        player.show_attributes()
        print('\n')
        sel = input('>>').lower()
        if sel == 'a':
            os.system('clear')
            player.set_room(cuarto_servidores.name)

        if sel == 'd':
            os.system('clear')
            player.set_room(pasillo_laboratorios.name)
        elif sel == '1':
            os.system('clear')
            juego_compu1.game(player)
        elif sel == '2':
            os.system('clear')
            juego_pizarra.game(player)
        elif sel == '3':
            os.system('clear')
            juego_compu2.game(player)

        elif sel == 'r': #easter egg R (palanca de cambios)
            os.system('clear')
            if 'borrador' not in player.inventory:
                player.add_to_inventory('borrador')
                player.add_lives(extra_life2)
            else:
                print('Ya reclamaste la vida extra')
        else:
            os.system('clear')

    elif player.room == cuarto_servidores.name and (player.lives > 0) and (player.winner == False):
        player.in_room(cuarto_servidores.name)

        print(cuarto_servidores_drawing)
        player.show_attributes()
        print('\n')
        sel = input('>>').lower()
        if sel == 'd':
            os.system('clear')
            player.set_room(laboratorio.name)

        elif sel == '1':
            os.system('clear')
            juego_rack.game(player)

        elif sel == '2':
            
            os.system('clear')
            juego_final.game(player)
        elif sel == '3':
            os.system('clear')
            juego_papelera.game(player)
        else:
            os.system('clear')


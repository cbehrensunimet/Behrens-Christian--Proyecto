import random
from Juego import*
import os

class Logica_emojis(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.requirement1 = game['requirement'][0]
        self.requirement2 = game['requirement'][1]
        self.msj = game['message_requirement']

    def game(self,player):



        '''
        Encuentra la lógica y resuelve
        Recibe: Diccionario del juego y objeto jugador
        Devuelve: True si el usuario completa el juego y False si se equivoca
        '''

        if self.award in player.inventory:
            return print('Ya tienes la recompensa de este juego!')

        if self.requirement1 in player.inventory and (self.requirement2 + ': Si estas gradudado puedes pisar el Samán') in player.inventory:
            print('Tienes los requisitos para jugar')
        else:
            print(self.msj)
            player.substract_lives(1)
            return False 

        eleccion = random.choice(['quiz1', 'quiz2'])
        pregunta1 = self.questions[0]
        pregunta2 = self.questions[1]
        recompensa = self.award
        respuesta1 = '67'
        respuesta2 ='41'
        print(self.name)

        if eleccion == 'quiz1':
            while True:
                
                print(pregunta1)
                answer = input('>>').lower()
                while not answer.isnumeric():
                    print('Respuesta inválida')
                    answer = input('Respuesta: ')

                if answer == respuesta1:
                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)
                    return True

                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    return False
        elif eleccion == 'quiz2':
            while True:
                
                print(pregunta2)
                answer = input('>>').lower()
                while not answer.isnumeric():
                    print('Respuesta inválida')
                    answer = input('Respuesta: ')

                if answer == respuesta2:
                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)
                    return True

                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    return False
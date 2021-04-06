import random
from Juego import*
import os

class Logica_Booleana(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.msj = game['message_requirement']

    def game(self,player):
        '''
        Juego Lógica Booleana
        Recibe: Diccionario del juego y objeto jugador
        Devuelve: True si el usuario completa el juego y False si se equivoca
        '''
        if self.requirement not in player.inventory:
           print(self.msj)
           return None
        elif self.award in player.inventory:
            print('Ya tienes la recompensa de este juego')
            return None
            
        quiz = random.choice(self.questions) #escoge un diccionario de la lista aleatoriamente
        recompensa = self.award

        print(self.name)
        print(self.rules)
        
        
        while True:
            pregunta = quiz['question']
            respuesta1 = quiz['answer']
            respuesta2 = lambda x: 'True' if x == 'False' else 'False'

            print(f'{pregunta}\n[A]{respuesta2(respuesta1)}\n[B]{respuesta1}')

            answer = input('Respuesta: [A] [B]\n>>').lower()
            while answer != 'a' and answer != 'b':
                print('Ingeso inválido')
                answer = input('Respuesta: [A] [B]\n>>').lower()

            if answer == 'b':
                os.system('clear')
                print('RESPUESTA CORRECTA')
                print('¡ROMPISTE EL CANDADO! Ahora la puerta está abierta')
                player.add_to_inventory(recompensa)
                return True
            else:
                os.system('clear')
                print('RESPUESTA INCORRECTA')
                player.substract_lives(1/2)
                return False
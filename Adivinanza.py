import random
from Juego import*
import os

class Adivinanza(Juego):
    def __init__(self, game, password):
        super().__init__(game)
        self.msj = game['message_requirement']
        self.password = password

    def game(self,player): #contraseña

        '''
        Juego de adivinanzas
        Recibe: Diccionario del juego y objeto jugador
        Devuelve: True si el jugador completa el juego y False si no lo completa o se queda sin vidas
        '''
        if self.award in player.inventory:
            os.system('clear')
            return print('Ya tienes la recompensa de este juego!')

        elif self.requirement != False:

            contraseña_usuario = input('Ingrese la contraseña de la computadora: ')
            if contraseña_usuario == str(self.password):
                print('Contraseña correcta!')
            else:
                print('Contraseña incorrecta')
                os.system('clear')
                print(self.msj)
                return False  
    
        
        recompensa = self.award
        quiz = random.choice(self.questions) #escoge un diccionario de la lista aleatoriamente
        pista1 = quiz['clue_1']
        pista2 = quiz['clue_2']
        pista3 = quiz['clue_3']
        pista = 0

        print(self.name)
        print(self.rules)

        while True:

            
            print(quiz['question'])
            
            hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
            while hint != 's' and hint != 'n':
                print('Ingreso inválido')
                hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
            if hint == 's':
                if player.hints > 0 and pista <= 3:
                    player.substract_hints(1)
                    pista +=1
                    if pista == 1:
                        print(pista1)
                    
                    elif pista == 2:
                        print(pista2)
                    
                    elif pista == 3:
                        print(pista3)
                    
                else:
                    print('No tienes pistas disponibles para este juego')
            if hint == 'n':
                answer = input('Respuesta: ').lower()

                if answer in quiz['answers']:
                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    
                    player.add_to_inventory(recompensa)
                    return True
                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    player.substract_lives(1/2)
                    return False

            if player.lives <= 0:
                return False
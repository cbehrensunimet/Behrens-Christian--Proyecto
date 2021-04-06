from Juego import*
import random
import time
import os

class Quiziz(Juego):
    def __init__(self, game):
        super().__init__(game)
    
    def game(self, player):
        '''
        Juego Quiziz cultura unimetana
        Recibe: Diccionario con datos del juego y objeto jugador
        Devuelve: True si el usuario completa el juego y False si se equivoca
        '''
        if self.award in player.inventory:
            return print('Ya tienes la recompensa de este juego')

        quiz = random.choice(self.questions) #escoge un diccionario de la lista aleatoriamente
        pistas_usadas = 0
        recompensa = self.award

        print(self.name)
        print(self.rules)

        while True:
            pregunta = quiz['question']
            respuesta1 = quiz['correct_answer']
            respuesta2 = quiz['answer_2']
            respuesta3 = quiz['answer_3']
            respuesta4 = quiz['answer_4']
            pista = quiz['clue_1']


            respuestas = [respuesta1,respuesta2,respuesta3,respuesta4]
            random.shuffle(respuestas)

            print(f'{pregunta}\n[A]{respuestas[0]}\n[B]{respuestas[1]}\n[C]{respuestas[2]}\n[D]{respuestas[3]}\n')
            

            hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
            while hint != 's' and hint != 'n':
                print('Ingreso inválido')
                hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
            if hint == 's':
                if player.hints > 0 and pistas_usadas == 0:
                    player.substract_hints(1)
                    print(pista)
                    pistas_usadas += 1 
                else:
                    print('No tienes pistas disponibles para este juego')

            answer = input('Respuesta: [A] [B] [C] [D]\n>>').lower()
            while answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd':
                print('Ingeso inválido')
                answer = input('Respuesta: [A] [B] [C] [D]\n>>').lower()

            if answer == 'a':
                if respuestas[0] == respuesta1:

                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)
                    return True
                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    player.substract_lives(1/4)
                    return False

            if answer == 'b':
                if respuestas[1] == respuesta1:

                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)
                    return True
                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    player.substract_lives(1/4)
                    return False
            if answer == 'c':
                if respuestas[2] == respuesta1:

                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)
                    return True
                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    player.substract_lives(1/4)
                    return False

            if answer == 'd':
                if respuestas[3] == respuesta1:

                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)
                    return True
                else:
                    os.system('clear')
                    print('RESPUESTA INCORRECTA')
                    player.substract_lives(1/4)
                    return False
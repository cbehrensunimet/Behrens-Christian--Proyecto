from fractions import Fraction
from sympy import *
from scipy.misc import derivative
from math import pi
from Juego import*
import random
import os


class Pregunta_matematica(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.msj = game['message_requirement']
        self.award = 'calculadora'
    
    def game(self,player):
        '''
        Juego preguntas matemáticas
        Recibe: Diccionario del juego y objeto jugador
        Devuelve: True si el usuario acierta la pregunta y False si no
        '''
        if self.requirement not in player.inventory:
           print(self.msj)
           return None

        elif self.award in player.inventory:
            print('Ya tienes la recompensa de este juego')
            return None
        else:

            quiz = random.choice(self.questions)
            pregunta = quiz['question']
            pistas_usadas = 0
            pista = quiz['clue_1']
            recompensa = self.award

            v = pregunta.split(' ') #lista
            v = v[7] #variable
            v = eval(v)

            x = Symbol('x')

            fn = pregunta.replace('Calcula la derivada de la función en ','') 
            fn = fn.replace('pi', '')
            fn = fn.replace('/3','')
            fn = fn.replace('f(x)=', '')
            fn = fn.replace('sen', 'sin')
            fn = eval(fn)


            respuesta = diff(fn, x).subs(x,v)                                   #(derivative(fn, v , dx=1e-5))
            respuesta = round(respuesta, 1)
            respuesta = str(respuesta)

  


            print(pregunta.replace('letra incorrecta', 'intento fallido'))
            
            while True:

                hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
                while hint != 's' and hint != 'n':
                    print('Ingreso inválido')
                    hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
                if hint == 's':
                    if player.hints > 0:
                        
                        if pistas_usadas == 0:
                            print(pista) 
                            player.substract_hints(1)
                            pistas_usadas +=1  

                        else:
                            print('No existen más pistas para esta pregunta')
                    else:
                        print('No tienes pistas disponibles para este juego')
                if hint == 'n':
                    answer = input('Respuesta: ')
                    while answer.isalpha():
                        print('La respuesta debe ser un número')
                        answer = input('Respuesta: ')
                    answer = answer.replace(',', '.')
                    answer = eval(answer)
                    answer = round(answer, 1)
                    answer = str(answer)
                    
                    if answer == respuesta:
                        os.system('clear')
                        print('RESPUESTA CORRECTA')
                        player.add_to_inventory('calculadora')
                        player.add_lives(1)
                        return True
                    elif answer != respuesta:
                        os.system('clear')
                        print('RESPUESTA INCORRECTA')
                        player.substract_lives(1/4)
                        return False
from Juego import*
import random
import os

class Palabra_desordenada(Juego):
    def __init__(self, game, password):
        super().__init__(game)
        self.password = password

    def game(self, player): # contraseña
        '''
        Juego Ordenar palabras
        Recibe: Diccionario del juego y clase jugador
        Devuelve: True si el jugador termina el juego y false si no
        '''
        if (self.award + ': ' + str(self.password)) not in player.inventory:

            recompensa = self.award
            quiz = random.choice(self.questions) #escoge un diccionario de la lista aleatoriamente

            pregunta = quiz['question']
            categoria = quiz['category']
            palabras = quiz['words']
            palabras_desordenadas = []
            palabras_adivinadas = []

            for palabra in palabras:
                lista = list(palabra)
                lista_desordenada = random.sample(lista, len(lista))
                palabra_desordenada = ''.join(lista_desordenada)
                palabras_desordenadas.append(palabra_desordenada)

            print(self.name.title())
            print(self.rules)
            print(f'\nCategoría: {categoria}\n')
            print('Palabras: ')
            for p in palabras_desordenadas: #imprime palabras desordenadas
                print(p)

            while player.lives > 0:

                answer = input('>>').lower()
                while not answer.isalpha():
                    print('Ingreso inválido')
                    answer = input('>>').lower()
                if answer in palabras_adivinadas:
                    print('Ya adivinaste esta palabra')

                elif answer in palabras:
                    palabras_adivinadas.append(answer)
                    print(f'PALABRA CORRECTA {len(palabras_adivinadas)}/{len(palabras)}')
                    print(f'Palabras Adivinadas: {" ".join(palabras_adivinadas)}')
                else:
                    print('PALABRA INCORRECTA')
                    player.substract_lives(1/2) 

                if len(palabras_adivinadas) == len(palabras):
                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa + ': ' + str(self.password))
                    return True

            os.system('clear')
            return False

        else:
            return print('Ya tienes la recompensa de este juego')

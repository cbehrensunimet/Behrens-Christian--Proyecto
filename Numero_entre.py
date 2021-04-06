from Juego import*
import random
import os 

class Numero_entre(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.award = game['award'].replace('í', 'i').title()
        
    
    def game(self,player):


        '''
        Juego Número Aleatorio
        Recibe: Diccionario del juego y objeto player
        Devuelve: True si el usuario completa el juego y False si se queda sin vidas
        '''
        if self.award not in player.inventory:
            
            pregunta = self.questions[0]['question']

            pistas = self.questions[0]['clue_1']
            pistas = pistas.split(',')

            nums = pregunta.split(' ')
            nums = nums[-1]
            nums = nums.replace('-', ',')
            nums = nums.split(',')
            num1 = int(nums[0])
            num2 = int(nums[1])
            numeros_adivinados = []
            recompensa = self.award
            
                
            respuesta = random.randint(num1,num2)
            fallos_seguidos = 0
            limit = 3
            print(self.name.title() + ' ' + str(num1) + ' y ' + str(num2))
            print(self.rules)
            while player.lives > 0:

                answer = input('Ingrese un número entero: ')
                while not answer.isnumeric():
                    print('Ingreso inválido')
                    answer = input('Ingrese un número entero: ')
                answer = float(answer)
                while not answer.is_integer():
                    print('Debe ingresar un número entero')
                    answer = input('Ingrese un número entero: ')
                answer = int(answer)

                if answer in numeros_adivinados:
                    print('Ya adivinaste este número')
                
                elif answer == respuesta:
                    os.system('clear')
                    print('RESPUESTA CORRECTA')
                    player.add_to_inventory(recompensa)

                    return True
                else:
                    fallos_seguidos += 1
                    numeros_adivinados.append(answer)
                    if (answer - respuesta) >= 5 and (answer - respuesta) > 0: #muy arriba
                        print(pistas[3])

                    elif (answer - respuesta) < 5 and (answer - respuesta) > 0 : #un poco arriba
                        print(pistas[1])

                    elif (answer - respuesta) <= -5 and (answer - respuesta) < 0: #muy abajo
                        print(pistas[2])

                    elif (answer - respuesta) > -5 and (answer - respuesta) < 0: #un poco abajo
                        print(pistas[0])

                if fallos_seguidos == limit:
                    player.substract_lives(1/4)
                    fallos_seguidos -= limit
            
            os.system('clear')
            return False

        else:
            print('Ya tienes la recompensa de este juego')
            return None
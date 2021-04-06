from Juego import*
import random
import os

class Pregunta_python(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.msj = game['message_requirement']
    
    def game(self,player):
        '''
        Juego preguntas python
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
            recompensa = self.award
            

            if len(quiz) == 5:
                pista = 0
                pista1 = quiz['clue_1']
                pista2 = quiz['clue_2']
                pista3 = quiz['clue_3']
                choice = 1
                frase = '\"tengo en mi cuenta 50,00 $\"'
                respuesta = 50 #int(float(frase.split(' ')[4].replace(',','.')))     
            else:
                pista = 0
                pista1 = quiz['clue_1']
                choice = 2
                frase = '\"oidutse ne al ortem aireinegni ed sametsis\" '
                respuesta = 'estudio en la metro ingenieria de sistemas' #" ".join([frase[slice(1,8)][::-1],frase[slice(9,11)][::-1], frase[slice(12,14)][::-1], frase[slice(15,20)][::-1], frase[slice(21,31)][::-1], frase[slice(32,34)][::-1], frase[slice(35,43)][::-1]])

            print((self.name).title())
            print(self.rules)

            print(pregunta)
            print('NOTA: Para referenciar la pregunta utilice la variable frase')

            while choice == 1:

                hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
                while hint != 's' and hint != 'n':
                    print('Ingreso inválido')
                    hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()

                if hint == 's':
                    if player.hints > 0 and pista < 3:
                        player.substract_hints(1)
                        pista +=1
                        
                        if pista == 1:
                            print(pista1)

                        elif pista == 2:
                            print(pista2) 

                        elif pista == 3:
                            print(pista3)
                        else:
                            print('No existen más pistas para esta pregunta')
                    else:
                        print('No tienes pistas disponibles para este juego')

                if hint == 'n':
                    answer = input('Respuesta: ')
                    try:
                        answer = eval(answer)

                    except:
                        print('error')
                        answer = None

                    if answer == respuesta:
                        
                        os.system('clear')
                        print('RESPUESTA CORRECTA')
                        player.add_to_inventory(recompensa)
                        return True
                    else:
                        
                        os.system('clear')
                        print('RESPUESTA INCORRECTA')
                        player.substract_lives(1/2)
                        return False


            while choice == 2:

                hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
                while hint != 's' and hint != 'n':
                    print('Ingreso inválido')
                    hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()

                if hint == 's':
                    if player.hints > 0 and pista < 1:
                        player.substract_hints(1)
                        pista +=1
                        
                        if pista == 1:
                            print(pista1)
                        else:
                            print('No existen más pistas para esta pregunta')
                    else:
                        print('No tienes pistas disponibles para este juego')
                if hint == 'n':
                    answer = input('Respuesta: ')
                    try:
                        answer = eval(answer)
                    except:
                        print('error')
                        answer = None

                    if answer == respuesta:
                        os.system('clear')
                        print('RESPUESTA CORRECTA')
                        player.add_to_inventory(recompensa)
                        return True
                    else:
                        os.system('clear')
                        print('RESPUESTA INCORRECTA')
                        player.substract_lives(1/2)
                        return False




            
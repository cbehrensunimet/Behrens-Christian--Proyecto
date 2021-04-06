from Juego import*
import random
import os

class Ahorcado(Juego):
    def __init__(self, game):
        super().__init__(game)

    def game(self, player):
        
        '''
        Juego Ahorcado
        Recibe: diccionario del juego y objeto jugador
        Devuelve: True si el jugador termina el juego; False si no lo termina o se queda sin vidas
        '''
        def mostrar_ahorcado(intentos):
            '''
            Muestra las fases del ahorcado en función de la canidad de intentos que lleve el usuario
            '''
            fases = ['''
            _____________
            │         │         
            │         0
            │        \│/
            │         │
            │        / \
           _│_  
            ''', '''
            _____________
            │         │         
            │         0
            │        \│/
            │         │
            │        / 
           _│_  
            ''', '''
            _____________
            │         │         
            │         0
            │        \│/
            │         │
            │        
           _│_  
            ''', '''
            _____________
            │         │         
            │         0
            │        \│/
            │         
            │        
           _│_  
            ''', '''
            _____________
            │         │         
            │         0
            │        \│
            │         
            │        
           _│_  
            ''', '''
            _____________
            │         │         
            │         0
            │         
            │         
            │        
           _│_  
            ''', '''
            _____________
            │         │         
            │         
            │        
            │         
            │        
           _│_  
            ''']
            return print(fases[intentos])


        if self.award not in player.inventory:
            
            recompensa = self.award
            quiz = quiz = random.choice(self.questions)
            pista1 = quiz['clue_1']
            pista2 = quiz['clue_2']
            pista3 = quiz['clue_3']
            pista = 0
            pregunta = quiz['question']
            adivina = False 
            letras_adivinadas =[]
            repuesta = quiz['answer'].lower()
            intentos = 6
            palabra_escondida = '_' * len(quiz['answer']) 

            print(self.name)
            print(self.rules)
            mostrar_ahorcado(intentos)
            print(f'Intentos: {intentos}')
            print(palabra_escondida)
            
            while intentos > 0:

                
                print(quiz['question'])
                
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
                        print('No tienes pistas disponibles para este juego')
                if hint == 'n':
                    answer = input('Ingrese una letra o palabra: ').lower()
                    while not answer.isalpha():
                        print('La respuesta solo contiene letras')
                        answer = input('Respuesta: ').lower()
                    
                    if len(answer) == 1:
                        if answer in letras_adivinadas: 
                            print('Ya adivinaste esta letra')

                        elif answer not in repuesta: #la letra no esta en la respuesta
                            print(f'La letra {answer} no está en la palabra')
                            intentos -= 1
                            letras_adivinadas.append(answer)
                            player.substract_lives(1/4)
                        else: #la letra esta en la respuesta
                            print(f'La letra {answer} está en la palabra')
                            letras_adivinadas.append(answer)
                            lista_palabra = list(palabra_escondida)
                            indices =[i for i, letra in enumerate(repuesta) if letra == answer] #seleccionar indices de la letra adivinada
                            for i in indices:
                                lista_palabra[i] = answer #sustituir letra adivinada en su posicion en la palabra
                            palabra_escondida = "".join(lista_palabra) #convertir a string la lista con la letra adivinada
                            if '_' not in palabra_escondida:
                                print('ADIVINASTE LA PALABRA!')
                                player.add_to_inventory(recompensa)
                                return True

                    elif answer == quiz['answer'].lower():
                        os.system('clear')
                        print('RESPUESTA CORRECTA')
                        player.add_to_inventory(recompensa)
                        return True
                    else:
                        print('RESPUESTA INCORRECTA')
                        player.substract_lives(1/4)
                        intentos -= 1
                    if player.lives <= 0:
                        return False

                    os.system('clear')
                    mostrar_ahorcado(intentos)
                    print(palabra_escondida)

            if intentos < 0:
                os.system('clear')
                print('INTENTOS AGOTADOS')
                print('Vuelve a intentarlo')
                return None


        else:
            os.system('clear')
            print('ya tienes la recompensa de este juego')
            return None
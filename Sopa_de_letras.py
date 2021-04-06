from Juego import*
import random 
import string
import os

class Sopa_de_letras(Juego):
    def __init__(self, game):
        super().__init__(game)
        
    def game(self,player):

        '''
        Sopa de Letras
        Recibe: Diccionario del juego y objeto jugador
        Devuelve: True si el jugador completa el juego y False si se queda sin vidas
        '''
        if self.award in (player.inventory):
            return print('Puedes jugar este juego solo una vez!')

        quiz = random.choice(self.questions)
        grid_size = 15
        
        
        words = [quiz['answer_1'].upper(), quiz['answer_2'].upper(), quiz['answer_3'].upper()] 
        
        def add_words(word, grid):
            '''
            Agrega la palabra deseada a la sopa de letras
            Recibe: palabra y grid
            Devuelve: grid con palabra 
            '''
            word = random.choice([word, word[::-1]])
            direction = random.choice([[1,0], [0,1],[1,1]]) #dirección en la que se dispone la palabra
            xsize = grid_size if direction[0] == 0 else grid_size - len(word) #tamaño de fila con o sin la palabra
            ysize = grid_size if direction[1] == 0 else grid_size - len(word) #tamaño de columna con o sin la palabra

            x = random.randrange(0,xsize) #posicion de la palabra en x
            y = random.randrange(0,ysize) #posicion de la palabra en y

            for i in range(0,len(word)):
                grid[y + direction[1] * i][x + direction[0] * i] = word[i] #poner la palabra en el grid
            return grid

        grid = [[random.choice(string.ascii_uppercase) for i in range(grid_size)] for j in range(grid_size)] #genera una matriz de nxn con letras aleatorias
        
        for word in words:
            grid = add_words(word, grid)
        
        print('SOPA DE LETRAS')
        print(self.rules)
        print('\n'.join(map(lambda row: ' '.join(row), grid))) #muestra sopa de letras completa

        pista1 = quiz['clue_1']
        pista2 = quiz['clue_2']
        pista3 = quiz['clue_3']
        pista = 0
        palabras_adivinadas = []

        while player.lives > 0:
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
                answer = input('Ingrese una palabra: ').upper()
                while not answer.isalpha():
                    print('La respuesta solo contiene letras')
                    answer = input('Ingrese una palabra: ').upper()

                if answer in palabras_adivinadas:
                    print('Ya adivinaste esta palabra')

                elif answer in words:
                    palabras_adivinadas.append(answer)
                    print(f'PALABRA CORRECTA {len(palabras_adivinadas)}/{len(words)}')
                    print(f'Palabras Adivinadas: {" ".join(palabras_adivinadas)}')

                    if len(palabras_adivinadas) == len(words):
                        os.system('clear')
                        print('RESPUESTA CORRECTA')
                        player.add_lives(1)
                        player.add_to_inventory(self.award)
                        return True
                else:
                    print('PALABRA INCORRECTA')
                    player.substract_lives(1/2)
        os.system('clear')
        return False
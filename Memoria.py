from Juego import*
import random
import os

class Memoria(Juego):
    def __init__(self, game):
        super().__init__(game)
    
    def game(self, player):
        '''
        Juego Memoria
        Recibe: Objeto jugador
        Devuelve: True cuando el usuario completa el tablero
        
        '''
        if self.award in player.inventory:
            return print('Ya tienes la recompensa de este juego')


        recompensa = self.award


        def show_grid(g):
                num = ['     0', '  1', '  2', '  3']
                print('   '.join(num))
                for j, linea in enumerate(g):
                        print(j, linea)
                print('\n')
        s_grid = [
        ['😀', '🙄', '🤮', '🥰'],
        ['🤮', '😨', '🤓', '😷'],
        ['😨', '🤓', '🥰', '😷'],
        ['🤑', '🤑', '🙄', '😀']
        ]

        grid = []

        e_grid = [
        ['--', '--', '--', '--'],
        ['--', '--', '--', '--'],
        ['--', '--', '--', '--'],
        ['--', '--', '--', '--']
        ]

        for l in s_grid:
                random.shuffle(l)
                grid.append(l)
        random.shuffle(grid)

        print(self.name.title())
        print(self.rules)
        show_grid(grid)

        l = input('Presione cualquier tecla cuando esté listo')
        os.system('clear')

        show_grid(e_grid)

        while player.lives > 0:

                x = input('Fila (X): ')
                while not x.isnumeric() or int(x) > (len(grid)-1):
                    print('Ingreso inválido')
                    x = input('Fila (X): ')

                y = input('Columna (Y): ')
                while not y.isnumeric() or int(y) > (len(grid)-1):
                    print('Ingreso inválido')
                    y = input('Fila (X): ')

                if e_grid[int(y)][int(x)] == '--':

                    e_grid[int(y)][int(x)] = grid[int(y)][int(x)] 
                    os.system('clear')
                    print(f'Coordenadas actuales: ({x},{y})')
                    show_grid(e_grid)
                    print('Encuentra su par')

                    if player.hints > 0:

                        hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
                        while hint != 's' and hint != 'n':
                                print('Ingreso inválido')
                                hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
                    else:
                        hint = 'n'

                    if hint == 'n':

                            i = input('Fila (X): ')
                            while not i.isnumeric() or int(i) > (len(grid)-1):
                                print('Ingreso inválido')
                                i = input('Fila (X): ')

                            j = input('Columna (Y): ')
                            while not j.isnumeric() or int(j) > (len(grid)-1):
                                print('Ingreso inválido')
                                j = input('Fila (X): ')

                            while e_grid[int(j)][int(i)] != '--':
                                print('Ya levantaste esta celda')
                                i = input('Fila (X): ')
                                while not i.isnumeric() or int(i) > (len(grid)-1):
                                    print('Ingreso inválido')
                                    i = input('Fila (X): ')

                                j = input('Columna (Y): ')
                                while not j.isnumeric() or int(j) > (len(grid)-1):
                                    print('Ingreso inválido')
                                    j = input('Fila (X): ')
                            
                            
                            e_grid[int(j)][int(i)] = grid[int(j)][int(i)]

                            if e_grid[int(j)][int(i)] == e_grid[int(y)][int(x)]:
                                os.system('clear')
                                print('CORRECTO')
                                
                                show_grid(e_grid)

                            else:
                                os.system('clear')
                                print('INCORRECTO')
                                player.substract_lives(1/4)
                                e_grid[int(j)][int(i)] = e_grid[int(y)][int(x)] = '--'
                                
                                show_grid(e_grid)
                    else:
                        player.substract_hints(1)
                        for i in range(len(grid)):
                                for j in range(i+1):
                                        if grid[int(y)][int(x)] == grid[i][j]:
                                                e_grid[i][j] = grid[i][j]
                                        elif grid[int(y)][int(x)] == grid[j][i]:
                                                e_grid[j][i] = grid[j][i]
                        os.system('clear')
                        show_grid(e_grid)
                                                
                else:
                    print('Ya volteaste esta celda')

                if e_grid == grid:
                        os.system('clear')
                        print('GANASTE')
                        player.add_to_inventory(recompensa)
                        return True
        os.system('clear')
        return False
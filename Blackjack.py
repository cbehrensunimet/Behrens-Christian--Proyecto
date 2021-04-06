from Juego import*
import random
import os
from art import*


class BlackJack(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.requirement1 = game['requirement'][0]
        self.requirement2 = game['requirement'][1]
        self.msj = game['message_requirement']
    
    def game(self, player):
        '''
        Blackjack 
        Recibe: objeto jugador
        Devuelve: True si el usuario gana y False si se queda sin vidas
        '''

        if self.requirement1 and self.requirement2 in player.inventory:
            print('Encontraste el cuarto secreto de la Universidad! pero esto es... ¡UN CASINO!')
            print('Para devolver los datos al sistema de la universidad deberás ganarle una partida de BlackJack a el dueño del casino... ¿Estás listo? ')
            tprint("casino",font="block",chr_ignore=True)
            op = input('Ingresa [S] cuando estés listo\n>>')
            while op != 's':
                print('Tómate tu tiempo... Ingresa [S] cuando estés listo')
                op = input('>>')

            print('Reglas: ')
            print('El objetivo de este juego es sumar 21 puntos o no pasarse de esta cifra, pero siempre sobrepasando el valor que tiene el dealer para ganar la apuesta.')
            print('Las cartas numéricas tienen en valor que indica la carta pero las demás tienen los siguientes valores:')
            print('A = 1; J , Q , K = 10; ☺ = 11')
            print('Por cada partida que pierdas perderás una vida')
            print('Que la suerte te acompañe!')

            while True:
                if player.lives > 0:

                    s = input('Presiona cualquier tecla para jugar una nueva mano: ')
                    os.system('clear')
                    
                    def show_card(c, s):

                        if c == 10:
                            c = random.choice(['J','Q','K']) #no uso el 10 porque descuadra el tamaño de la carta
                        elif c == 11:
                            c = '☺'
                        elif c == 1:
                            c = 'A'

                        return print(f''' 
                     _______
                    |{c}      |
                    |       |
                    |   {s}   |
                    |       |
                    |      {c}|
                     ‾‾‾‾‾‾‾
                    ''')

                    def back_card():
                        return print(f''' 
                     _______
                    |♦♦♦♦♦♦♦|
                    |♦♦♦♦♦♦♦|
                    |♦♦♦♦♦♦♦|
                    |♦♦♦♦♦♦♦|
                    |♦♦♦♦♦♦♦|
                     ‾‾‾‾‾‾‾
                    ''')

                    dealer_cards = []
                    player_cards = []

                    #cartas del dealer
                    while len(dealer_cards) != 2:
                        dealer_cards.append(random.randint(1,11))
                        if len(dealer_cards) == 2:
                            print('Cartas del Dealer: ')
                            show_card(dealer_cards[0], random.choice(['♠', '♥', '♦', '♣']) ) #muestra cartas del dealer
                            back_card()

                    #cartas del jugador
                    while len(player_cards) != 2:
                        player_cards.append(random.randint(1,11))
                        if len(player_cards) == 2:
                            print('Tus cartas: ')
                            for c in player_cards:
                                show_card(c, random.choice(['♠', '♥', '♦', '♣']) ) #muestra cartas del jugador
                            print(f'Suma: {sum(player_cards)}')

                    #sumar cartas del dealer
                    if sum(dealer_cards) == 21:
                        print('BLACKJACK! El dealer suma 21')
                        print('EL DEALER GANA')
                        player.substract_lives(1)
                        

                    elif sum(dealer_cards) > 21:
                        print('El dealer se pasó!')
                        print('GANASTE')
                        player.set_winner()

                    else:
                        #sumar cartas del jugador
                        while sum(player_cards) < 21:
                            answer = input('[P] Pedir otra carta\n[Q] Quedarte\n>>').lower()
                            while answer != 'p' and answer != 'q':
                                print('Ingreso inválido')
                                answer = input('>>')
                            if answer == 'p':
                                player_cards.append(random.randint(1,11))
                                print('Nueva carta: ')  
                                show_card(player_cards[-1], random.choice(['♠', '♥', '♦', '♣']) ) #muestra cartas del jugador
                                print(f'Suma: {sum(player_cards)}')

                            else:
                                print(f'La suma del dealer es de {sum(dealer_cards)} con valores de {dealer_cards} ')
                                print(f'Tu suma total es de {sum(player_cards)} con valores de  {player_cards} ')
                                if sum(player_cards) < sum(dealer_cards):
                                    print('EL DEALER GANA')
                                    player.substract_lives(1)
                                    
                                else:
                                    print('GANASTE')
                                    player.set_winner()
                                    return True

                        if sum(player_cards) > 21:
                            print('Te pasaste! El dealer gana ')
                            player.substract_lives(1/2)
                            
                        elif sum(player_cards) == 21:
                            print('BLACKJACK! Ganaste la partida')
                            player.set_winner()

                else:
                    os.system('clear')
                    break

            return False
        else:  
            print(self.msj) 
            return None
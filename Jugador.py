from Usuario import *

class Jugador(Usuario):
    def __init__(self, username, password, age, avatar, lives, hints, difficulty, room):
        super().__init__(username, password, age, avatar)

        self.finish_time = None
        self.lives = lives
        self.hints = hints
        self.difficulty = difficulty
        self.room = room
        self.inventory = []
        self.winner = False
        self.in_biblioteca = 0
        self.in_laboratorio = 0
        self.in_pasillo = 0
        self.in_plaza = 0
        self.in_servidores = 0
        self.times_played = 0

    def set_room(self, new_room):
        self.room = new_room

    def add_to_inventory(self, object):
        print(f'Se ha añadido {object} al inventario!')
        self.inventory.append(object)
    
    def set_winner(self):
        self.winner = True
    
    def add_lives(self, quantity):
        if quantity == 0:
            print('Ya reclamaste esta vida extra')
        else:
            print(f'+{quantity} vida(s)')
            self.lives += quantity
    
    def substract_lives(self, quantity):
        print(f'-{quantity} vida(s)') 
        self.lives -= quantity
    
    def substract_hints(self, quantity):
        print(f'-{quantity} pista(s)') 
        self.hints -= quantity

    def show_attributes(self):
        inv = ", ".join(self.inventory)
        c = int(self.lives*4)
        v = '■'*c
        print(f'Pistas: {self.hints}\nVida: {v}\nInventario: {inv}')

    def set_time(self, finish_time):
        self.finish_time = finish_time

    def in_room(self, room):
        if room == 'biblioteca':
            self.in_biblioteca +=1
        elif room == 'plaza_rectorado':
            self.in_plaza +=1
        elif room == 'laboratorio':
            self.in_laboratorio +=1
        elif room == 'pasillo_laboratorios':
            self.in_pasillo +=1
        elif room == 'cuarto_servidores':
            self.in_servidores +=1

    def add_in_room(self, room, quantity):
        if room == 'biblioteca':
            self.in_biblioteca +=quantity
        elif room == 'plaza_rectorado':
            self.in_plaza +=quantity
        elif room == 'laboratorio':
            self.in_laboratorio +=quantity
        elif room == 'pasillo_laboratorios':
            self.in_pasillo+=quantity
        elif room == 'cuarto_servidores':
            self.in_servidores +=quantity

    def add_play(self):
        self.times_played +=1

    def graph_room_in(self):
        b = '■' *self.in_biblioteca
        pl = '■' *self.in_plaza
        l = '■' *self.in_laboratorio
        pa = '■' *self.in_pasillo
        s = '■' *self.in_servidores

        print(f'{self.username}\n')
        print(f'Biblioteca:\n{b} {self.in_biblioteca}\nPlaza Rectorado:\n{pl} {self.in_plaza}\nPasillo Laboratorio:\n{pl} {self.in_pasillo}\nLaboratorio SL-001:\n{l} {self.in_laboratorio}\nCuarto Servidores:\n{s} {self.in_servidores}')
        
    def graph_plays(self):
        p = '■' *self.times_played
        print(f'{self.username}\n{p} {self.times_played}')
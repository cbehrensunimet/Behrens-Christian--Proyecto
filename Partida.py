class Partida:
    def __init__(self, username, winner, difficulty, time):
        self.username = username
        self.winner = winner
        self.difficulty = difficulty
        self.time = time


    def winner(self):
        self.winner = True

    def set_time(self, time):
        self.finish_time = time

    def show(self):
        if self.winner:
            g = 'Sí'
        else:
            g = 'No'
        print(f'Usuario: {self.username}\nGanador: {g}  Dificultad: {self.difficulty} Tiempo: {self.time}')


def set_difficulty():
    d = input('Ingrese el valor de la dificultad en la que desea jugar\n1-Fácil\n2-Intermedio\n3-Difícil\n4-Imposible\n>>')
    while d != '1' and d != '2' and d != '3' and d != '4':
        print('Ingreso inválido')
        d = input('Ingrese el valor de la dificultad en la que desea jugar\n1-Fácil\n2-Intermedio\n3-Difícil\n4-Imposible\n>>')

    if d == '1':
        d = 'facil'

    elif d == '2':
        d = 'intermedio'

    elif d == '3':
        d = 'dificil'

    elif d == '4':
        d = 'imposible'

    return d

def set_time(difficulty):
    with open('difficulty.txt', 'r') as f:
        for line in f:
            if line.split(',')[0] == difficulty:
                time = line.split(',')[1]
                time = time.replace(' ', '')
                time = time.replace('minutos', '')
                return int(time)

def set_lives(difficulty):
    with open('difficulty.txt', 'r') as f:
        for line in f:
            if line.split(',')[0] == difficulty:
                lives = line.split(',')[2]
                lives = lives.replace(' ', '')
                lives = lives.replace('vidas', '')
                
                if int(lives) == 0:
                    print('IMPOSIBLE, no puedes jugar con 0 vidas')
                    return None

                return int(lives)

def set_hints(difficulty):
    with open('difficulty.txt', 'r') as f:
        for line in f:
            if line.split(',')[0] == difficulty:
                hints = line.split(',')[3]
                hints = hints.replace(' ', '')
                hints = hints.replace('pistas', '')
                return int(hints)

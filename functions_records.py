from functions_user import *
from Partida import*
import matplotlib.pyplot as plt

def new_match(matches, player):
    '''
    Guarda los datos de la partida y los mete en la lista macthes
    '''
    match = Partida(player.username, player.winner, player.difficulty, player.finish_time)
    matches.append(match)
    return matches

def new_record(records, player):
    '''
    Guarda los datos del jugador en lista records y devuelve la lista actualizada
    '''
    player.add_play()
    records.append(player)
    return records

def update_records(records, player):
    '''
    Actualiza los atributos de los objetos guardados en la lista records
    '''
    for record in records:
        if record.username == player.username:
            record.add_in_room('biblioteca', player.in_biblioteca )
            record.add_in_room('plaza_rectorado', player.in_plaza )
            record.add_in_room('laboratorio', player.in_laboratorio )
            record.add_in_room('pasillo_laboratorios', player.in_pasillo)
            record.add_in_room('cuarto_servidores', player.in_servidores)
            record.add_play()
    
    return records

def top_matches(matches):
    '''
    Muestra el top 5 de las mejores partidas
    Recibe: Lista de partids
    Devuelve: None
    '''
    w_matches = []

    if len(matches)==0:
        return print('VACÍO')

    for p in matches:
        if p.winner == True:
            w_matches.append(p)

    if len(w_matches) == 0:
        return print('NO HAY VICTORIAS REGISTRADAS')

    matches_s = sorted(w_matches, key=lambda match: match.time)   # ordenar por tiempo de menor a mayor
    for i, match in enumerate(matches_s):
        if i < 5:
            print(f"{i+1}-")
            match.show()
        print('\n')

def cuartos_mas_visitados(records):
    
    if len(records) == 0:
        return print('VACÍO')
    for record in records:
        record.graph_room_in()
        '''
        x = [record.in_biblioteca, record.in_pasillo, record.in_laboratorio, record.in_plaza, record.in_servidores]
        l = ['Biblioteca', 'Pasillo de los laboratorios', 'Laboratorio SL-001', 'Plaza Rectorado', 'Cuarto de Servidores']
        e = (0.1, 0.1, 0.1, 0.1,0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(x, explode=e, labels=l, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal') 
        print('GRAFICA')
        plt.show()
        '''
        print('\n')



def partidas_usuarios(records):

    if len(records) == 0:
        return print('NO HAY PARTIDAS DISPONIBLES')

    records_s = sorted(records, key=lambda record: record.times_played, reverse=True)   # ordenar por veces jugadas de mayor a menor
    for i, record in enumerate(records_s):
        print(f'{i+1}-')
        record.graph_plays()
    print('\n')
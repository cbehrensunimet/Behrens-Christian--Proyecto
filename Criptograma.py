from Juego import*
import string
import random
import os

class Criptograma(Juego):
    def __init__(self, game):
        super().__init__(game)
        self.msj = game['message_requirement']
    
    def game(self,player):
        '''
        Juego criptograma
        Recibe: diccionario del juego, objeto jugador
        Devuelve: True si el usuario acierta y False si falla 
        '''
        if self.requirement not in player.inventory:
           print(self.msj)
           return None
        elif self.award in player.inventory:
            print('Ya tienes la recompensa de este juego')
            return None

        quiz = random.choice(self.questions) #escoge un diccionario de la lista aleatoriamente
        recompensa = self.award
        
        texto = (quiz['question']).lower()
        texto = texto.replace("á", "a")
        desplazamiento = quiz['desplazamiento']

        abc = string.ascii_lowercase #abecedario en minúscula
        cifrado = "" #texto cifrado vacío
        for c in texto:
            if c in abc:

                cifrado = cifrado + abc[(abc.index(c) + desplazamiento )%(len(abc))] #desplazamiento de las letras
            else:
                cifrado = cifrado + c

        print(self.name.title())
        print(self.rules)

        print("El cifrado César, es una de las técnicas de cifrado más simples y más usadas. Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Por ejemplo, con un desplazamiento de 3, la A sería sustituida por la D (situada 3 lugares a la derecha de la A), la B sería reemplazada por la E, etc. ")
        print("\n")
        print(f"Texto cifrado: {cifrado}")
        print(f'Desplazamiento: {desplazamiento}')
        answer= input("Respuesta: ").lower()
    
        if answer == texto:
            os.system('clear')
            print(f"RESPUESTA CORRECTA")
            player.add_to_inventory(recompensa)
            return True
        else:
            os.system('clear')
            print("RESPUESTA INCORRECTA" )
            player.substract_lives(1)
            return False
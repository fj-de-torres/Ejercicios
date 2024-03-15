import random

def make_dice_cup(sides=6, dice=1):
    def roll():
        '''Roll the dice'''
        return tuple(random.randint(1, sides) for _ in range(dice))
    
    return roll

d6 = make_dice_cup(dice=2)
dato_tirada = d6() #Esto es una *core function* en otros lenguajes: funciones ejecutadas por partes. Se ejecuta una función que necesita una función que fabrica otra en base a los primeros argumentos que se le pasan, y luego en la siguiente fase, los argumentos para la función interna.
print(dato_tirada)
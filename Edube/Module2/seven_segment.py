from os import system
system("cls || clear")
leds = {
    1 : ['  #','  #','  #','  #','  #'],
2 : ['###','  #','###','#  ','###'],
3 : ['###','  #','###','  #','###'],
4 : ['# #','# #','###','  #','  #'],
5 : ['###','#  ','###','  #','###'],
6 : ['###','#  ','###','# #','###'],
7 : ['###','  #','  #','  #','  #'],
8 : ['###','# #','###','# #','###'],
9 : ['###','# #','###','  #','###'],
0 : ['###','# #','# #','# #','###']
}

def led_number(n:str):
    n = str(n)
    # for digito in n:
    #     if digito.isdigit():
    # digits= [numero for numero in n]
    # #print(digits)
    
    for i in range(5):
        for numero in n:
            print(leds[int(numero)][i],end=" ")
        print()
    print()

led_number(123)
#print(leds['1'])
led_number(9081726354)
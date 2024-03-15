from os import system
system("cls || clear")


def led_number(n:str,char="#"):
    full = '■'*3
    c_s_c = char+" " + char
    s_s_c = " "*2 + char
    c_s_s = char + " " * 2
    leds = {
    1 : [s_s_c for i in range(5)],
2 : [full,s_s_c,full,c_s_s,full],
3 : [full,s_s_c,full,s_s_c,full],
4 : [c_s_c,c_s_c,full,s_s_c,s_s_c],
5 : [full,c_s_s,full,s_s_c,full],
6 : [full,c_s_s,full,c_s_c,full],
7 : [full,s_s_c,s_s_c,s_s_c,s_s_c],
8 : [full,c_s_c,full,c_s_c,full],
9 : [full,c_s_c,full,s_s_c,full],
0 : [full,c_s_c,c_s_c,c_s_c,full]
}
    n = str(n)
    # for digito in n:
    #     if digito.isdigit():
    # digits= [numero for numero in n]
    # #print(digits)
    
    for i in range(5):
        for numero in n:
            print(leds[int(numero)][i],end="  ")
        print()
    print()
led_number(123,'❚')
#print(leds['1'])
led_number(9081726354,'❚')
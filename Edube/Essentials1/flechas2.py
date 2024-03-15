""" a = " "*4+"*"+" "*4
b = " "*3+"* *"+" "*3
c = " "*2+"*   *"+" "*2
d = "*"*3+" "*3+"*"*3
e = " "*2+"*"+" "*3+"*"+" "*2
g = " "*2+"*"*5+" "*2
a = "       *       "
    "      **      "
a3= "     *  *     "
a1= "    *    *    "
    "   *      *   "
b2= "  *        *  "
d1= " * *      * * *"
e1= "   *      *    "
e2= "   *      *    "
f1= "   *      *    "
g1= "   ********   "
space_in_between = "  "

n = 6
veces= 3 """
""" print((a+space_in_between)*3)
print((b+space_in_between)*3)
print(c,c,sep=space_in_between)
print(d,d,sep=space_in_between)
[print(e,e,sep=space_in_between) for i in range(2)]
print(g,g,sep=space_in_between) """
# [print((i+space_in_between)*n) for i in flecha]
# [print((i+space_in_between)*n) for i in flecha]
#for contador in range(veces):
    # for i in flecha:
    #     print((i+space_in_between)*n)
def flechas_a_tutiplen(fila:int,columna:int):
    a = " "*4+"*"+" "*4
    b = " "*3+"* *"+" "*3
    c = " "*2+"*   *"+" "*2
    d = ("*"+" "*0)*3+" "*3+"*"*3
    e = " "*2+"*"+" "*3+"*"+" "*2
    g = " "*2+"*"*5+" "*2
    space_in_between = "  "
    flecha = [a,b,c,d,e,e,g]
    [[print((i+space_in_between)*fila) for i in flecha] for columna in range(columna)]

flechas_a_tutiplen(6,1)

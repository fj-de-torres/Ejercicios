import os
so.system("cls || clear")

def linea(h_length:int) -> str:
    print("💝"*h_length)

def column(col_length: int,col_number: int,square_width:int) -> str:
    for i in range(col_number):
        for i in range(col_length):
                print("💖",end="")
                print(" "*square_width,end="")
           
linea(22)
column(3,2,6)
        
    
    #for i in range(3):
    #    for i in range(10):
    #        print("💝",end="")
    #print()
#for i in range(3):
#        print("💝"*9)
#print("💖")

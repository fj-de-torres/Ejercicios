#𝕱𝖗𝖆𝖓𝖈𝖎𝖘𝖈𝖔 𝕵. 𝖉𝖊 𝕿𝖔𝖗𝖗𝖊𝖘
class Vehiculo:
       
    def __init__(self,make:str,model:str,year:str,colour:str) -> None:
        self.__make = make
        self.__model = model
        self.__year = year
        self.__colour = colour

    def get_make(self):
        return self.__make
   
    def get_model(self):
        return self.__model
  
    def get_year(self):
        return self.__year
    
    def get_colour(self):
        return self.__colour
    

from dog import Dog
from spider import Spider

if __name__ == "__main__":
    snoopy = Dog("Snoopy")

# La clase abstracta no se puede instanciar:
# Traceback (most recent call last):
#   File ".../Ejercicios/session16/abstracto/app.py", line 4, in <module>
#     snoopy = Dog("Snoopy")
# TypeError: Can't instantiate abstract class Dog with abstract method num_legs
#Una clase que viene de una abastractar que no impleenta los métodos de la abstracta, que ha de implementar, también es abstracta.

    snoopy = Dog("Snoopy")
    print(snoopy.num_legs())

    snoopy.eat() #Porque es otro método de la clase abstracta que está implementado.

    arana = Spider()
    print(arana.num_legs())
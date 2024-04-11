
from os import system
from colorama import Fore, Back, Style

def clear():
    system("clear")

def myprint(string:str):
    print(Fore.YELLOW + "\n"+ f"{string}" +"\n" + Fore.WHITE)
class Foo:
    a = 33
    def foo_method(self):
        print(id(self))

clear()
print(Foo.a)
mylist = [1,2,3]

Foo.foo_method(mylist)
print(id(mylist))

print(Fore.YELLOW + """\nNormalmente, los métodos ejecutan operaciones en instancias de clase, por lo que generalmente reciben la instancia como un argumento y luego la procesan:\n"""+ Fore.WHITE)

f = Foo()
Foo.foo_method(f)

myprint("""Pasar la instancia el método es la operación en la que se basa la programación orientada a objetos, y por esta razón ha sido definida una sintaxis alternativa que permite pasar la instancia al método de forma automática. Según esta convención, cuando un método es llamado directamente mediante la instancia, esta se pasa al método como *primer* argumento. Es decir, la llamada Foo.foo_method(f) tiene el mismo efecto que la siguiente:""")

f.foo_method()

myprint("""Como veremos más adelante, este comportamiento no siempre es así, porque existe un tipo de métodos denominados métodos de clase, a los cuales siempre se pasa la clase como primer argumento, incluso cuando están calificados mediante la instancia""")


myprint("""En este caso, como hemos podido ver, la instancia f se ha pasado a Foo.foo_method(). De hecho, esto es lo que ocurre cuando se intenta llamar mediante la instancia a un método que no acepta argumentos:""")

class Foo:
    def foo_method():
        print('python')
Foo.foo_method()
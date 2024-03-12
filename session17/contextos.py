# Context managers:

from contextlib import contextmanager
from os import system
from colorama import Fore, Back, Style

@contextmanager
def my_context_manager():
    print("Entrando en el contexto")
    val = object()
    print(id(val))
    try:
        yield val
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Saliendo del contexto")


with my_context_manager() as ctx:
    print("Dentro del contexto")
    print(id(ctx))
    raise Exception("Horror desde el 'with' context")
    print('Después de lanzadao el error del "raise", esto no se va a ejecutar')

print(Fore.YELLOW + "Fuera del contexto" + Fore.WHITE)


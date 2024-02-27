class Cliente:

    def __init__(self, nombre: str, dni: str) -> None:
        self.__nombre = nombre
        self.__dni = dni

    def __str__(self):
        return f"{self.__nombre}|{self.__dni}"

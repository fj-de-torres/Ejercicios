class Documento:
    def __init__(self, contenido) -> None:
        self.__contenido = contenido


class PortaDocumentos:
    def __init__(self, color) -> None:
        self.__documentos = [] 
        self.__color = color

    def anyadir_documento(self, doc: Documento):
        self.__documentos.append(doc)


class Abogado:
    def __init__(self, nombre, porta: PortaDocumentos) -> None:
        self.__nombre = nombre 
        self.__portadocumentos = porta

    
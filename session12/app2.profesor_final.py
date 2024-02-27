from examen import Examen
from profesor import Profesor

if __name__ == "__main__":
    
    examen_mates = Examen('Matematica')
    examen_literatura = Examen('Literatura')
    examen_ingles = Examen('English')

    profe_juan = Profesor('Juan', 'Mates')


    examenes_corregidos = profe_juan.corregir_examenes(examen_mates, examen_literatura)

    for index, examen in enumerate(examenes_corregidos, start=1):
        print(f"{examen.tema}_{index}" , examen.nota, sep=":")



"""
asignaturas = ["mates", "literatura"]
PREFIX = "examen_"

profe_juan = Profesor('Juan', 'Mates')

lista = list()
for asig in asignaturas:
    lista.append(Examen.crear_examen(asig))
else:
    examenes_corregidos = profe_juan.corregir_examenes(*lista)
    for examen in examenes_corregidos:
        print(examen.tema , examen.nota, sep=":")
    

"""


"""
1) El profesor podrá corregir varios examenes
2) Modularizar el app
"""

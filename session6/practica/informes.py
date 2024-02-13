def mostrar_promedios_por_asignatura(promedios:list):
    for asignatura,promedio in promedios: #destructuring
        print("*"*15,"Promedios","*"*15)
        print(f"Asignatura: {asignatura}")
        print("-"*55)
        print(f"Promedio: {promedio}")
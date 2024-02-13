def mostrar_promedios_por_asignatura(promedios: list):
    print("*" * 15, "Promedios", "*" * 15)
    for asignatura,promedio in promedios:
        print("-" * 55)
        print(f"Asignatura:{asignatura}")
        print(f"Promedio:{promedio}")


from calculadora import sumar, restar, sumar_v2
#import calculadora as calc

def calcular(x: int = 0, y: int = 0, z: int = 0) -> int:
    return x + y + z

def matricular_alumnos(curso: dict,**d_alumnos):
    curso.update(d_alumnos)
    return curso

if __name__ == "__main__":

    alumnos = {
        "111H": "juan",
        "222H": "maria",
        "333H": "jaime"

    }

    #matricular nuevos alumnos
    nuevos_alumnos = {
        "444H": "luis",
        "555H": "silvia",
    }
    print(f"ANTES MAT:{alumnos}")
    alumnos = matricular_alumnos(curso=alumnos,**nuevos_alumnos)
    print(f"DESPUES MAT:{alumnos}")

    print("-" * 50)
    
    #resultado = calc.sumar(10,3)
    resultado = sumar(10,3)
    print(f"Resultado:{resultado}")

    resultado = sumar_v2(10,3,1,1,1,1,1,1,1,1,1)
    print(f"Resultado_sumarv2:{resultado}")

    valores_a_sumar = [2,5,2,8,0]
    resultado = sumar_v2(*valores_a_sumar)

    #resultado = calc.restar(10,3)
    resultado = restar(10,3)
    print(f"Resultado:{resultado}")

    resultado2 = calcular(3)
    print(f"Resultado2:{resultado2}")


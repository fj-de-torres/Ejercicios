# Repaso de métodos estáticos, etc
```
class Counter(self):
    count = 10
```
Esto está perteneciendo sólo a la clase, no a las instancias, pues no está dentro del __init__

La instancia puede hacer uso e incluso cambiar ese valor. Pero si lo cambia, ya lo hace suyo. Ya no accederá al valor general:
```
    def __init__(self):
    Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(),cls()]
        print(f"Se han creado {cls.count} instancias")
        return two:counters
```

```
c1 = Counter()
print(c1.count)

c2 = Counter()
print(c2.count)
```
Resultado:
> 10
> 10
```
c1, c2 = Counter.create_two()


x, y = c1.create_two()
print(type(x), type(y))
```
Resultado:

> Se han creado 2 instancias
> Se han creado 4 instancias
> <class '__main__.Counter'> <class '__main__.Counter'>

```
class Receta():

    def __init__(self, patata, huevo):
        self.__patata = patata
        self.__huevo = huevo
        self.__cebolla = cebolla

    @classmethod
    def receta_sin_cebolla(cls, n_papatas=2, n_huevos=4):
        return cls(n_papatas,n_huevos,0)

    @classmethod
    def receta_con_mas_huevo(cls):
        return cls(2,6,1)
```
ese método declase nos deja hacer una instanciación modificada de la clase inicial
```
primer_plato = Receta(2,4,1)
tortilla_sin_cebolla = Recta.receta_sin_cebolla()
tortilla_sin_cebolla = Receta.receta_sin_cebolla(n_papatas=3)
```
## Métodos estáticos:

```
class Tiempo_Atmosferico():
    def __init__(self, temperaturas):
        self.__temperaturas = temperaturas #farenheit
        
    staticmethod
    def convert_from_faren_to_celsius(temp_f):
        calculation = round((temp_f - 32) / 1.8,2)
        return calculation
```
Los métodos estáticos se usan internamente por la propia clase. Los mmétodos estáticos también se pueden acceder a ellos desde las instancias (con un self).
```
    def in_celsius(self):
        return [convert_from_faren_to_celsius(temp) for temp in self.__temperaturas]
```
Instanciamos la clase:
```
t_at = Tiempo_Atmosferico([56.55,45.90,68.90,32.10])
temps_celsius = t_at.in_celsius()
print(temps_celsius)
```
Resultado:

> [13.64, 7.72, 20.5, 0.06]

¿Puedo utilizar la temperatura desde fuera? Sí:
```
temp_c = Tiempo_Atmosferico.convert_from_faren_to_celsius(56.55)
print(temp_c)
```
Resultado:

> 13.64

Esto en Java no se puede hacer desde la clase. Esto implica que no se debería hacer en python aunque se pueda.

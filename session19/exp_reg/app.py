from os import system
import re
def clear():
    system("cls || clear")
#Esto es case-sensitive
#Se detiene en la primera aparicón.
print(re.search('python','Me gusta mucho aprender python ya que me permitirá ganarme la vida como Master Developer del Universo (y de python)')) 
#Para que muestre todas las apariciones:
print(re.findall('python','Me gusta mucho aprender python ya que me permitirá ganarme la vida como Master Developer del Universo (y de python)'))

# print(re.findall('m*','Me gusta mucho aprender python ya que me permitirá ganarme la vida como Master Developer del Universo (y de python)'))

print(re.match('python', 'Me gusta mucho aprender python ya que me permitira ganarme la vida como developer')) #No hay match porque lo busca a principio de la cadena

for match in re.finditer('python', 'Me gusta mucho aprender python ya que me permitira ganarme la vida como developer python'):
    #print(match.start(), match.end())
    print(match)

#\w -> palabras
print("\tHola\nAdios")
# Para que los caracteres anteriores no tengan una función de caracteres no imprimibles, hacermos:
print(r"\Hola\nAdios")

## Búsquedas usando expresiones regulares:
#Quiero encontrar dígigos (el primero o todos dependiendo de qué metodo utilice)
#Aquí también estoy utilizando la expresión *r* que pide que no lo tome como caracter no imprimible, y así se tome como expresión regular.
clear()
pattern = re.compile(r'\d')
sentence = "En el summary test de Python Essential 1 he sacado un 8"

print(pattern.findall(sentence))
#Ahora deseo encontrar todo lo que no sea dígito: con \D

pattern = re.compile(r'\D')

print(*pattern.findall(sentence))
#No palabras (\W):
pattern = re.compile(r'\W')
print(pattern.findall(sentence))
clear()
pattern = re.compile(r'La sandia')

match = pattern.match('La sandia que compre el otro dia estaba muy dulce')

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


    #print("La encontré")

sentece = "Mi correo es ricardo@gmail.com y el correo de mi hermano es hermano@gmail.com"
pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')


print(pattern.findall(sentece))


from sys import path
import os
os.system("cls || clear")
#os.system("export $PYTHONPATH = ~/Documents/Learning/Python/Ejercicios/Edube/Module2/")
path.append("./extrapack.zip")
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI as funI
from extra.good.beta import FunB as funB

print(sig.FunS())
print(alp.FunA())
print(funI())
print(funB())
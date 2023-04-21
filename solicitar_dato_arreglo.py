import random
from array import array
arreglo=array("f",[])
largo=random.randint(10,30)
print(largo)
for i in range(0,largo):
    numero=random.randint(0,100)
    arreglo.append(numero)
print(arreglo)
dato=int(input(("escoga el elemento a solcitar ente el rango de 0 " +" y",largo-1)))
print(arreglo[dato])
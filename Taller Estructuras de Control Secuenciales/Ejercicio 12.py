"""
Entradas:
MATEMATICAS
Examen matem--->float--->matex
tarea 1--->float--->mat1
tarea 2--->float--->mat2
tarea 3--->float--->mat3

FISICA
examen fisica--->float--->fiex
tarea 1--->float--->fi1
tarea 2--->float--->fi2

QUIMICA
examen quimica--->float--->quimex
tarea 1--->float--->quim1
tarea 2--->float--->quim2
tarea 3--->float--->quim3

Salidas:
Promedio matematicas--->float--->avmat
promedio fisica--->float--->avfi
promedio quimica--->float--->avquim
promedio general--->float-promedio
"""

#Datos de entrada
print("Matematicas: ")
matex=float(input("Nota del examen: "))
mat1=float(input("Nota de la tarea 1: "))
mat2=float(input("Nota de la tarea 2: "))
mat3=float(input("Nota de la tarea 3: "))


print("Fisica: ")
fiex=float(input("Nota del examen: "))
fi1=float(input("Nota de la tarea 1: "))
fi2=float(input("Nota de la tarea 2: "))


print("Quimica: ")
quimex=float(input("Nota del examen: "))
quim1=float(input("Nota de la tarea 1: "))
quim2=float(input("Nota de la tarea 2: "))
quim3=float(input("Nota de la tarea 3: "))

#Caja negra Matematicas
avmat=(matex*0.9)+(((mat1+mat2+mat3)/3)*0.1)

#Caja negra fisica
avfi=(fiex*0.8)+(((fi1+fi2)/2)*0.2)

#Caja negra quimica
avquim=(quimex*0.85)+(((quim1+quim2+quim3)/3)*0.15)
prom=((avmat+avfi+avquim)/3)

#Datos de salida
print("Promedio Matematicas: "+str(avmat))
print("Promedio Fisica: "+str(avfi))
print("Promedio Quimica: "+str(avquim))
print("Promedio General: "+str(prom))
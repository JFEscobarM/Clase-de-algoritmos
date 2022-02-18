"""
Datos de entrada
Mujeres-->int-->Mujeres
Hombres-->int-->Hombres

Caja negra
Total-->tot-->int
Porcentaje de mujeres-->PM-->int
porcentaje de hombres-->PH-->int

Salidas
print-->porcentaje de mujeres-->PM-->int
print-->porcentaje de hombres-->PH-->int
"""
#Datos de entrada
M=int(input("Numero de mujeres: "))
H=int(input("Numero de hombres: "))

#Caja negra
Tot=(M+H)
PM=(M/Tot)*100
PH=(H/Tot)*100

#Datos de salida 
print("Porcentaje de mujeres: ",(PM), "Porcentaje de de hombres: ",(PH))
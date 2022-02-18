"""
Daros de entrada
precio de contado--->float--->P
valor de la cuota mensual--->float--->T

Caja negra 
precio cuotas--->float--->pr
recargo--->float--->r
porcentaje de recargo--->float--->por

Datos de salida
print--> "el porcentaje de recargo-->por-->float
"""
#Datos de entrada
P=float(input ("Digite el precio de contado:" ))
T=float(input ("Digite el valor de la cuota mensual: "))

#caja negra
pr=(T*12)
r=(pr-P)
por=((r*100/P))

#Datos de salida
print("El porcentaje de recargo es: ",(por), "%")
"""
Datos de entrada
precio final--->float--->pfin
precio de venta--->float--->pventap

Caja negra
diferencia--->float--->dif
porcentaje descuento--->float--->d

Datos de salida
print-->float-->d
"""
#Datos de entrada
pfin=float(input ("Digite el valor pagado: "))
pventp=float(input ("Ingrese el precio de venta sugerido: "))

#Caja negra
dif=(pventp-pfin)
d=((dif*100)/pventp)

#Datos de salida
print("El porcentaje de descuento fue: ",(d))
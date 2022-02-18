"""
Datos de entrada:
venta en galones--->float--->gal

Caja negra
venta en litros--->float--->lts
total venta--->float--->tot

Datos de salida
Print-->tot-->float
"""
#Datos de entrada
gal=float(input ("Ingrese la venta en galones: "))

#Caja negra
lts=(gal*3.785)
tot=(lts*50000)

#Datos de salida
print("El total de la venta es: ",(tot))
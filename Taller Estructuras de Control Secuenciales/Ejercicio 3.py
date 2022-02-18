"""
Datos de entrada
venta1-->float-->v1
venta2-->float-->v2
venta3-->float-->v3
sueldobase-->float-->sb

Caja negra
comisión-->float-->c
total-->float-->tot

Datos de salida
Print-->comision-->c-->float
print-->sueldo total-->tot-->float
"""
#Datos de entrada
v1=float(input("Digite la venta1: "))
v2=float(input("Digite la venta2: "))
v3=float(input("Digite la venta3: "))
sb=float(input("Digite el sueldo base: "))

#caja negra
c=((v1+v2+v3)/3)*0.10 
tot=sb+c

#Datos de salida
print("La comision es: ",(c)," Sueldo total: ",(tot))
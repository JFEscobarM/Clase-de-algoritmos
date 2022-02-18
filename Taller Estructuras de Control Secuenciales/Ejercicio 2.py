"""
Datos de entrada-->capital-->c-->float

caja negra-->c*02-->s1-->ganacia 
suma de la ganancia-->s2

datos de salia--> el total de dinero-->float-->s2
"""
#Datos de entrada
C=float(input("Ingrese su capital"))

#Caja negra
s1=(C*0.2)
s2=(s1+C)

#datos de salida
print("El total de dinero ganado ",s2)

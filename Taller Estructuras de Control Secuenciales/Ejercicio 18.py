"""
Entradas:
Capital-->float-->c
tiempo-->int-->T
tasa-->float-->Ta

Salidas:
Interes-->float-->In
Promedio-->float-->p
"""
#Datos de entrada
C=float(input("Insertar capital: "))
T=int(input("Insertar el tiempo de inversión: "))
Ta=float(input("Insertar la tasa de interes: "))

#Caja nagra
In=((C*Ta*T)/100)
P=(In/T)

#Datos de salida
print("El valor total de ineteres es: ",(In), "El porcentaje de interes por año es: ",(P), "%")
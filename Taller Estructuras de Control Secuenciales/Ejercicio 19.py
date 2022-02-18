"""
Entradas:
cantidad de naranjas--->int--->X
precio por docena--->float--->Y
valor venta--->float--->K

Salidas:
numero de docenas--->float--->docena
costo--->float--->precio
ganancia--->float--->ganancia
porcentaje ganancia--->float--->p
"""
X=int(input ("Numero de naranjas: "))
Y=float(input ("Valor por docena: "))
K=float(input ("Valor de las ventas: "))
docena=(X/12)
p=(Y*docena)
g=(K-p)
p=((g*100)/p)
print("El porcentaje de ganancias es: ",(p), "%")
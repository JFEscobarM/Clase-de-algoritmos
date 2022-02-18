"""
Datos de entrada
Venta-->float-->Venta

Descuento-->float-->D
Valor total-->float-->total

Datos de salida
print-->descuento -->D
print-->valor a pagar-->tot
"""
#Datos de entrada
Venta=float(input("Digite la venta: "))

#Caja negra
D=(Venta*0.15)
tot=(Venta-D)

#Datos de Salida
print("valor de descuento: ",(D)," valor a pagar: ",(tot))
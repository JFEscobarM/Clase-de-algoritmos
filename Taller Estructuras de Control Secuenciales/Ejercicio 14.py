"""
Datos de entradaa
Lectura_Anterior --> Float --> L1
Lectura_Actual --> Float --> L2
Precio_Kilovatio --> Float --> P


Salidas
Cantidad_Pagar --> Float --> Cp
"""

# Entradas
L1= float(input("Digite la lectura del mes pasado: "))
L2 = float(input("Digite la lectura actual: "))
P= float(input("Digite el costo del kilovatio: "))

# Caja negra
Cp = (L1-L2)*P

# Salidas
print("El monto a pagar en el mes es de: ",(Cp)("$"))
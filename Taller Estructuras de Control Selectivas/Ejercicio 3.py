"""
Datos de entradas: 
A --> int --> A 
B --> int --> B 
C --> int --> C 
D --> int --> D

Datos de salidas: 
Resultado de la operación --> float --> E
"""

# Entradas 
A = int(input("\nDigite el valor de A "))
B = int(input("Digite el valor de B "))
C = int(input("Digite el valor de C "))
D = int(input("Digite el valor de D "))

# Caja negra 
if D == 0:
    E = (A-C)**2
else: 
    E = ((A-B)**3)/D
    
# Salidas 
print(f"El resultado es {E} cuando D es igual a {D} \n")    
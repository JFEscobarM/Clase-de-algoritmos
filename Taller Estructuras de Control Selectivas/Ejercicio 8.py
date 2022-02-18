"""
Datos de entrada: 
P --> int --> P 
Q --> int --> Q

Datos de salida: 
P --> str --> P 
Q --> str --> Q 
"""

# Entrada 
P = int(input("\nDigite el valor de P "))
Q = int(input("Digite el valor de Q "))

# Caja negra
if P**3 + Q**4 - (2*(P**2)) > 680:
    # Salida
    print(str(P) + " y " + str(Q) + " satisfacen la expresión\n")
else: 
    # Salida
    print(str(P) + " y " + str(Q) + " no Satisfacen la expresión\n")
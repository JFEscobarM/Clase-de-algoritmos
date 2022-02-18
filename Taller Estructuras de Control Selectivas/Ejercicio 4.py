"""
Datos de entrada: 
Costo total --> float --> A 

Datos de salida: 
Fondos de la empresa --> float --> B
Cantidad a pagar a credito --> float --> C 
Intereses --> float --> D 
Prestamo del banco --> float --> E
"""

# Entradas 
A = float(input("\nDigite el valor total de la compra "))

# Caja negra 
if A > 5000000:
    B = float(A*.55)
    C = float(A*.25)
    E = float(A*.30)
    D = float(C*.20)
else:
    B = float(A*.70)
    C = float(A*.30)
    D = float(C*.20)
    E = 0

# Salida 
print(f"\nLos fondos utilizados de la empresa son: {B} \nEl credito al fabricante es de: {C} \nPor intereses del fabricante tenemos {D}\nEl prestamo del banco es: {E}\n")
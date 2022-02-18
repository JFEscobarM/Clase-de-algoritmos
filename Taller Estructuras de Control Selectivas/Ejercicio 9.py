""" 
Datos de entrada: 
Nombre --> str --> A
Compra --> float --> B

Datos de salida: 
Total --> float --> C 
Nombre --> str --> A 
Compra --> float --> B 
Descuento --> float --> D
"""

# Entrada 
A = str(input("\nDigite tu nombre "))
B = float(input("Digite el valor de tu compra "))

# Caja negra 
if B < 50000:
    D = 0
elif 50000 <= B < 100000:
    D = .05 
elif 100000 <= B < 700000:
    D = .11 
elif 700000 <= B < 1500000:
    D = .18
else: 
    D = .25

C = B - B * D 

# Salida 
print(f"\nHola {A}\nPara la compra: {B}\nEl valor a pagar es: {C}\nCon un descuento de: {B*D}\n")
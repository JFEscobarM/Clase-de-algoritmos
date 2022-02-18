"""
Datos de entrada:
A --> float --> A 
B --> float --> B
C --> float --> C

Datos de salida: 
X1 --> float --> E
X2 --> float --> F
"""

# Entradas
A = float(input("\nDigite el valor de A "))
B = float(input("Digite el valor de B "))
C =  float(input("Digite el valor de C "))

# Caja negra
D = B**2 -4*A*C
if D == 0:
    E = F = -B/(2*A)
elif D > 0: 
    E = (-B + (B**2 -4*A*C)**0.5)/(2*A)
    print(E)
    F = (-B - (B**2 -4*A*C)**0.5)/(2*A)
else: 
    E = F = "No tiene solución en los reales"

# Salidas
print(f"\nEl valor de X1 es: {E}\nEl valor de X2 es: {F}\n") if D >= 0 else print(E,"\n") 
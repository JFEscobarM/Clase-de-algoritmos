"""
Datos de entrada:
Kilometros --> float --> A 

Datos de salida: 
Precio --> float --> B
"""

# Entrada 
A = float(input("\nDigite los kilometros recoridos "))

# Caja negra 
if A <= 300: 
    B = 50000 
elif 1000 > A > 300:
    B = 70000 + 30000 * (A - 300)
else: 
    B = 150000 + 9000 * (A - 1000)
    
# Salida 
print(B)
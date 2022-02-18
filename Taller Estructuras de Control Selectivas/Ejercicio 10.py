"""
Datos de entrada:
Sueldo --> float --> A

Datos de salida:
Nuevo sueldo --> float --> B 
Categoría --> int --> C
"""
# Entrada 
A = float(input("\nDigite tu sueldo bruto "))

# Caja negra
if A <= 900000:
    B = A + A*.60
    C = 5
elif 2000000 >= A > 900000:
    B = A + A*.40
    C = 4
elif 3600000 >= A > 2000000:
    B = A + A*.20
    C = 3
elif 4300000  >= A > 3600000:
    B = A + A*.15
    C = 2
else:
    B = A + A*.10
    C = 1
    
# Salida 
print(f"\nSu sueldo es {C}\nTu nuevo sueldo es de {B}\n")
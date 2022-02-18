"""
Datos de entradas:
A --> str --> A
B --> str --> B
C --> str --> C
D --> str --> D 

Datos de salida: 
N --> int --> N
"""

# Entradas
A = str(input("\nDigite el valor de A "))
B = str(input("Digite el valor de B "))
C = str(input("Digite el valor de C "))
D = str(input("Digite el valor de D "))

# Caja negra
N = A + B + C + D
N = int(N)

if N <= (int(A) * 1000 + int(B)*100 + 50):
    N = N - int(C + D) 
else:
    Dn = N - ((int(A)*1000)+ (int(B)*100))
    N = N + 100 - Dn


# Salida 
print(f"\nEl resultado redondeado es ",N)
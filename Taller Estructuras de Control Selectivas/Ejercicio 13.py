"""
Datos de entrada: 
Anterior --> float --> A
Actual --> float --> B 

Datos de salida: 
Total --> float --> C
"""

# Entrada 
A = float(input("\nDigite la lectura anterior "))
B = float(input("Digite la lectura actual "))
D = (B-A)

# Caja negra 
Valor = [4600, 80000, 100000, 120000]
lista = [0, 100, 300, 500, 100, 300, 500, 1000000000000000000000000000000000] # El ultimo valor para representa infinito

for i in range(4):
    if lista[i] <= D <= lista[4 + i]:
        C = D * Valor[i]

# Salida
print("La cantidad a pagar es de",C,"\n")
"""
Datos de entrada: 
COP --> float --> A
Datos de salida: 
A descompuesto --> str --> lista0
"""

# Entrada 
A = float(input("\nDigite una cantidad en COP "))

# Caja negra 
lista = []
for i in [100000,50000,20000,10000,5000,2000,1000,500,200,100,50]:
    if A >= i: 
        lista.append(int(A/i)*i)
        A = A - int(A/i)*i
    else: 
        A = A
lista0 = str(lista)[1: -1]

# Salida
print(lista0,"\n")
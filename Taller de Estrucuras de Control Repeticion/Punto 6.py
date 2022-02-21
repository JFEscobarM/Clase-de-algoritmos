"""
Datos de entrada
Dividendo-->int-->A
Divisor-->int-->B

Datos de salida
Resto-->int-->A
cociente-->int-->N

"""
# Datos de entrada 
A = int(input("Digite el dividendo "))
B = int(input("Digite el divisor "))

# Caja negra
print()
C = int(A/B)
N = 0
for i in range(C):
    print("{A} - {B} = {A-B}")
    A = A - B
    N += 1

# Datos de salida
print("El resto de la división es ",A)
print("El cociente de la dicisión es ",N)
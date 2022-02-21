"""
Datos de entrada
Numero mayor-->int-->N
Numero menor-->int-->K

Datos de salida
Enteros de N a K-->int-->N
"""
#Datos de entrada
N=int(input("Digite el numero menor desde el cual se desea hacer la cuenta "))
K=int(input("Digite el numero mayor hasta el cual se terminara la cuenta "))

#Caja negra

while K >= N:
    print("\nN tiene que ser mayor que K ")
    N = int(input("Digite nuevamente N "))
    K = int(input("Dgitie nuevamente K "))
    
D = N - K + 1
for i in range (D):
    print(N) # Salidas
    N -= 1
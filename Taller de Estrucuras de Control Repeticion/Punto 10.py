"""
Datos de entrada
numero-->int-->n

Datos de salida
print-->lista 
"""
lista=[0,1]
n=int(input("numero 1 para agregar una altura y numero 2 para buscar el numero mas grande"))
while True:
    if(n==1):
        n=int(input("altura"))
        n=int(input("numero 1 para agregar una altura y numero 2 para buscar el numero mas grande"))
        lista.append(n)
    elif(n==2):
        print("el numero es:", max(lista)) 
        break

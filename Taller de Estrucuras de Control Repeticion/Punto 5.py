"""
Datos de salida

"""
e = 1
while True:
    d = ((e**2)+1)/e
    if d > 1000:
        e -= 1
        d = ((e**2)+1)/e
        break
    else: 
        print(e)
        e += 1
# Salidas
print("El numero de terminos necesarios es:",e)
print("El resultado de la sumatoria es:",d)
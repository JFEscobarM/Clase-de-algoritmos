"""
Datos de entrada
Edades-->e1,e2,e3-->int

caja negra
suma de las edades divida en tres-->emd-->float

datos de salida
Media de las edades-->emd-->float
"""
#datos de entrada
e1=int(input("Digite su edad"))
e2=int(input("Digite su edad"))
e3=int(input("Digite su edad"))

#caja negra
emd=float(e1+e2+e3)/3

#datos de salida
print("el promedio de las edades es ",emd)
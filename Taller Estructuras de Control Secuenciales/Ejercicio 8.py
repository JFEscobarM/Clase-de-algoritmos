"""
Datos de entrada:
lado a-->float-->a
lado b-->float-->b
lado c-->float-->c

Caja negra
semiperimetro-->float-->S
area-->float-->A

Datos de salida
print-->A-->float
"""
#Datos de entrada
a=float(input("Insertar valor de lado a: "))
b=float(input("Insertar valor de lado b: "))
c=float(input("Insertar valor de lado c: "))

#Caja negra
S=((a+b+c)/2)
A=((S*(S-a)*(S-b)*(S-c))**0.5)

#Datos de salida
print("El area del triangulo es: ",(A))
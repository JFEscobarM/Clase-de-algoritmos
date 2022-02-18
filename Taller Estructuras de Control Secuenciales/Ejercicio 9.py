"""
Datos de entrada
Horas trabajadas--->float--->horast
precio--->float--->precio

Caja negra
Salario bruto--->float--->sb
descuentos--->float--->d
salario neto--->float--->tot

Datos de salida
Print-->float-->tot
"""
horast=float(input("Ingrese el numero de horas trabajadas: "))
precio=float(input("Ingrese el valor por cada hora de trabajo: "))
sb=(horast*precio)
d=(sb*0.2)
tot=(sb-d)
print("El salario total es: ",(tot))
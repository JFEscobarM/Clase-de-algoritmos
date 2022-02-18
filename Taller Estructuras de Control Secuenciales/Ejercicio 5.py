"""
Datos de entrada
Parcial1-->float-->P1
Parcial2-->float-->P2
Parcial3-->float-->P3
Examenfinal-->float-->E
Trabajofinal-->float-->T

Caja negra
Promedioparciales-->float-->Promp
Notadefinitiva-->float-->Notafinal

Datos de salida
Print-->Nota final-->float-->N
"""

#Datos de entrada
P1=float(input("Nota del parcial 1: "))
P2=float(input("Nota del parcial 2: "))
P3=float(input("Nota del parcial 3: "))
E=float(input("Nota examen final: "))
T=float(input("Nota del trabajo final: "))

#Caja negra
Promp=((P1+P2+P3)/3)
N=((Promp*0.55)+(E*0.33)+(T*0.15))

#Datos de salida
print("Nota definitiva: ",(N))
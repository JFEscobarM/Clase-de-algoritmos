
"""
Datos de entrada
Chelines-->float-->CHE
Dracmas-->Float-->DRA
Pesetas-->float-->PST
"""
#Datos de entrada

CHE=float(input("Ingrese el valor en chelines para cambiarlos a pesetas: "))
DRA=float(input("Ingrese el valor en dracmas para cambiarlos a francos: "))
PST=float(input("Escriba el valor en pesetas para pasarlo a dolares y liras italianas: "))

#Caja negra
V1=((CHE*956871)/100)
v2=((DRA*88607)/100)
v3=(v2/20110)
v4=(PST*122499)
v5=(PST*9289)/100

print("El valor total de chelines a pesetas es: ",(V1))
print("El valor de dracmas a francos es: "(v3))
print("El valor de pesetas a dolares es: ",(v4)),("y a liras italianas es:",v5) 

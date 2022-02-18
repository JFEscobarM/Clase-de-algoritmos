"""
Datos de entrada
a-->str-->Nombre del trabajador
b-->int-->Hora normal en pesos
c-->int-->Horas normales trabajadas
d-->int-->Horas extras trabajadas
e-->int-->Cantidad de hijos

Caja negra
b*c-->f-->int
d*(b+(b*0.25))-->g-->float
f-(f*.014)-->h-->float
h+250000+(173000*e)+180000+g-->i-->float

Datos de salida
i-->int-->Salario final
"""
#Datos de entrada
a=str(input("Digite el nombre del trabajador: "))
b=int(input("Digite pago por hora trabajada:" ))
c=int(input("Digite cantidad de horas trabajadas: "))
d=int(input("Horas extras trabajadas: "))
e=int(input("Digite la cantidad de hijos: "))

#caja negra
f=b*c
g=d*(b+(b*0.25))
h=f-(f*.014)
i=h+250000+(173000*e)+180000+g

#Datos de salida
print("El sueldo total del trabajador es de ",(i))
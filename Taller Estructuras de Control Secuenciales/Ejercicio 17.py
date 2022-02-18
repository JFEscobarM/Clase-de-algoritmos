"""
Datos de entrada:
Presupuesto total--->float--->presup

Caja negra:
presupuesto ginecologia--->float--->g
presupuesto traumatologia--->float--->t
presupuesto pediatria--->float--->p

Datos de salida
print-->g-->float
print-->t-->float
print-->p-->float
"""
#Datos de entrada
presup=float(input ("Digite el valor del presupuesto total anual "))

#Caja negra
g=(presup*0.4)
t=(presup*0.3)
p=(presup*0.3)

#Datos de salida
print("El presupuesto de ginecologia es: ",(g))
print("El presupuesto de traumatologia es: ",(t))
print("El presupuesto de pediatria es: ",(p))
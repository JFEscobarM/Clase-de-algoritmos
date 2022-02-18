"""
Datos de entradas: 

Float-->dinero invertido ; intereses
Dinero invertido  --> float --> D
Intereses del banco --> float --> Int

Datos de salidas:
El dinero total en el banco
Dinero total --> float --> C
"""

# Entradas
D = float(input("Cuanto dinero tiene invertido en el banco "))
Int = float(input("Cuales son los intereses (%) de su banco por inversión "))

# Caja negra 
B = Int/100
C = D * B
E = C + D

# Salidas 
print("\nEl dinero de tu cuenta es",E,"\n")  if C > 100000 else print("\nEl dinero de tu cuenta es",D,"\n")
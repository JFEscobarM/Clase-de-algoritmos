"""
Datos de entrada:
Temperatura --> float --> Temp

Datos de salida: 
Deporte --> str --> B
"""

# Entrada 
Temp = float(input("\nDigite tu temperatura en Farenheit "))

# Caja negra 
if Temp > 85:
    B = "Natación"
elif 70 < Temp <= 85:
    B = "Tenis"
elif 32 < Temp <= 70:
    B = "Golf"
elif 10 < Temp <= 32:
    B = "Esquí"
else: 
    B = "Marcha"

# Salida 
print("\n" + B + "\n")
"""
Datos de entrada
contraseña-->int-->A

Datos de salida
Si la contraseña es incorrecta-->"senha invalida"
Si la contraseña es correcta-->"acesso permitidio"

"""
# Datos de entrada
A = int(input())

# Caja negra
while A != 2002:
    print("Senha Invalida") # Salida
    A = int(input())

# Salida
print("Acesso Permitido")
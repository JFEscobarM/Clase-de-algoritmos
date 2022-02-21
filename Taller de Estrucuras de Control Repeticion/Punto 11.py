"""
Datos de entrada
se pregunta si la persona consume licor-->int-->licor
licor preferido-->int-->licorp
edad-->int-->edad
sexo-->int-->sexo
continuar con la investigacion-->int-->se
"""

while True:
    licor=int(input("Consume licor?\nDigite 0 para SI y 1 para NO "))
    if licor==0:
        
        licorp=int(input("Licor preferido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)"))
        edad=int(input("Edad "))
        sexo=int(input("Sexo\nDigite 0 si es MUJER y 1 si es HOMBRE "))


    elif licor==1:
        
        edad=int(input("Edad "))
        sexo=int(input("Sexo\nDigite 0 si es MUJER y 1 si es HOMBRE "))


    se=int(input("Desea seguir con la investigacion?\nDigite 0 para SI y 1 para NO ")) 
    if se==1:
        break
        
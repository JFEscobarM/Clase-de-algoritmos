usuarios = { 
    "iperurena": { 
        "nombre": "Iñaki", 
        "apellido": "Perurena",
        "password":"123123"
    }, 
    "fmuguruza": { 
        "nombre": "Fermín", 
        "apellido": "Muguruza", 
        "password": "654321" 
     }, 
    "aolaizola": { 
        "nombre": "Aimar", 
        "apellido": "Olaizola", 
        "password": "123456" 
    } 
} 
for i in usuarios:
    usuario=input("Ingrese usuario ")
    contraseña=input("Ingrese contraseña ")

    if usuario in usuarios and contraseña==usuarios[usuario]["password"]:
        print(usuarios[usuario]["nombre"],usuarios[usuario]["apellido"])
        break
    else:
        print("Incorrecto")
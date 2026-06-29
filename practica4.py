continuar = "si"
invitacion = input ("¿posee invitacion?")
while continuar == "si":
    edad = int (input("ingrese la edad:"))
    invitacion == input ("¿posee invitacion?(si/no):").lower()
    if edad >= 18 and invitacion == "si":
        print ("acceso permitido.")
    else: 
        print ("acceso denegado.")

    continuar = input ("¿desea verificar otra persona? (si/no):").lower()
    print ("programa finalizado.")

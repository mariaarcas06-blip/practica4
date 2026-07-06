pin_correcto = 4321
contador_intentos = 0
max_intentos = 3

#pedir mientras queden intentos
while intentos < max intentos: 
     
# pedir pin al usuario
pin_ingresado = int (input("ingrese su pin:"))
if pon ingresado =pin correcto:
    print ("acceso concedido")
break 
else: print ("pin incorrecto")
intentos += 1

if intentos == max_intentos:
    print ("targeta bloqueda")

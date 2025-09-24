#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#  Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Ingresa un numero"))
divisor = int(input("Ingreso un segundo numero"))

if divisor == 0:
    print("Error")

else:
    print(dividendo/divisor)
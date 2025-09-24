message = "bienvenidos al circo"
print("a" in message) #preguntamos si el carater a existe en la variable mensaje

message_copia = message[:] #usamos el shadow copy para copiar el string
print(message_copia)

#Uso de f strings
edad = 12
print(f"tu tienes {edad} años") # se usa para interpolacion
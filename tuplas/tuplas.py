materias = ("ingles", "matematicas", "sociales", "ciencias")
print(materias)

#imprimimos cada valor que contiene los indices

print(materias[0])
print(materias[1])
print(materias[2])
print(materias[3])

#uso de la funcion zip no permite generar tuplas a partir de otras collecciones de datos
calificaciones = (3,6,7,1,0,10)
personal = ["maestros", "director", "secretarios", "personal de limpieza"]

# usando la funcion zip vamos a hacer que las colecciones "personal" y "calificaciones" generen nuevas tuplas

nueva_tupla = tuple(zip(calificaciones, personal))
print(nueva_tupla)

#tambien podemos usar la funcion len en las tuplas

print(len (calificaciones))

#sorted lo que va a ser es devolver la tupla con los datos ordenados de forma ascendente

print(sorted(calificaciones))


#count() nos permite saber cuantos elementos hay en la tupla

print(calificaciones.count(3))

print(9 in calificaciones) #verificamos que exista 0 en la tupla

print(calificaciones.index(3)) #nos permite saber el valor que contiene el indice 3
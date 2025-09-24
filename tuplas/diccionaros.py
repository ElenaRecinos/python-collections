expediente = {
                 'nombre' : 'Reynold',
                 'apelido' : 'Echkard',
                 'edad' : 20,
                 'altura' :1.80,
                 'peso' :77,
                 'estatus' :True

             }




print(expediente)
print(expediente['nombre']) # Accedemos al dato con la llave
print(expediente['apelido'])

print('edad' in expediente)

# metodo keys nos permite vizualizar las llaves de un diccionario
print(expediente.keys()) #output:['nombre', 'apelido', 'edad', 'altura', 'peso', 'estatus'])

# metodo values nos permite ver los valores que estan en las llaves
print(expediente.values()) #output:(['Reynold', 'Echkard', 20, 1.8, 77, True])

#metodo items nos permite ver tanto las llaves como los valores del diccionario
print(expediente.items())  #output: ([('nombre', 'Reynold'),('apelido', 'Echkard'), ('edad', 20), ('altura', 1.8), ('peso', 77), ('estatus', True)])
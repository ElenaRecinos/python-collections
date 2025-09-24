lista_principal = [[1,2], [3,4], [5,6], [2,4]] #[1,2], [3,4], [5,6], [2,4] sublistas
print(lista_principal)

#Slicing
lista2 = [1, 2, 3, 4, 5, 6]
sublista = lista2[1:4] # no se toma el valor del indice 4 solo del 1 , 2 y 3
print(sublista)


#Shadow copy
lista2_copia = lista2[:] #genera una copia de la lista original
print(lista2_copia)

#unir listas
lista_secundaria = [[2,4] , [6,7]]
lista_principal.extend(lista_secundaria)
print(lista_principal)

#eliminar valores de las listas
lista2.remove(3)
print(lista2)

#Copiar listas
numeros = lista2.copy
print(numeros)

#revertir orden de los elementos de la lista
lista2.reverse()
print(lista2)